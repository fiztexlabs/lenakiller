import numpy as np
from math import *
from scipy import linalg
import RGPPY as rgp


class CoilHE:
    """
    Стационарная модель змеевикового теплообменника
    ----------

    v0.1.1
    
    Arguments
    ----------
    lambda_w (float): Теплопроводность стенки теплообменных трубок [Вт/м]
    T_in_t_in (float): Температура теплоносителя на входе в внутритрубное пространство [К]
    T_out_t_in (float): Температура теплоносителя на входе в межтрубное пространство [К]
    P_in_t_in (float): Давление теплоносителя на входе в внутритрубное пространство [Па]
    P_out_t_in (float): Давление теплоносителя на входе в межтрубное пространство [Па]
    G_in_t_in (float): Расход теплоносителя на входе в внутритрубное пространство [кг/с]
    G_out_t_in (float): Расход теплоносителя на входе в межтрубное пространство [кг/с]
    mode (bool): Режим работы теплообменника (1 - противоток, 0 - прямоток)
    n_razb (int): Количество разбиений по участкам для расчета
    geometry (dict): Массив геометрических характеристик трубного пучка
        {
            d_in_t (float): внутренний диаметр теплообменных трубок [м]
            d_out_t (float): наружный диаметр теплообменных трубок [м]
            s_hor (float): горизонтальный шаг трубок [м]
            s_vert (float): вертикальный шаг трубок [м]
            n_ryad_vert (int): количество рядов в трубном пучке по вертикали
            a_avg (float): средний угол навивки змеевиков [град]
            D_avg (float): средний диаметр навивки змеевиков [м]
            L_t (float): средняя длина трубок [м]
            n_t (int): количество теплообменных трубок в пучке
            F_he_in_t (float): площадь теплообменной поверхности по внутритрубному пространству [м2]
            F_he_out_t (float): площадь теплообменной поверхности по межтрубному пространству [м2]
            F_in_t (float): площадь проходного сечения по внутритрубному пространству [м2]
            F_out_t (float): площадь теплообменной поверхности по межтрубному пространству [м2]
        }
    
    Attributes
    ----------
    subst_in_t: Объект для расчета свойств среды в внутритрубном пространстве
    subst_out_t: Объект для расчета свойств среды в межтрубном пространстве
    
    Methods
    ----------

    .. autosummary::
       :toctree: generated/

       evaluate - make next timestep for ejector model
    """
    def __init__(
                self,
                lambda_w: float,
                T_in_t_in: float,
                T_out_t_in: float,
                P_in_t_in: float,
                P_out_t_in: float,
                G_in_t_in: float,
                G_out_t_in: float,
                n_razb: int,
                mode = 1,
                geometry: dict = {
                    "d_in_t": float,
                    "d_out_t": float,
                    "s_hor": float,
                    "s_vert": float,
                    "n_ryad_vert": int,
                    "a_avg": float,
                    "D_avg": float,
                    "L_t": float,
                    "n_t": int,
                    "F_he_in_t": float,
                    "F_he_out_t": float,
                    "F_in_t": float,
                    "F_out_t": float
                },
                alw_in_t = 4.5e3,
                alw_out_t = 5.5e3,
            ):
        self.geometry = geometry
        self.lambda_w = lambda_w
        self.T_in_t_in = T_in_t_in
        self.T_out_t_in = T_out_t_in
        self.P_in_t_in = P_in_t_in
        self.P_out_t_in = P_out_t_in
        self.G_in_t_in = G_in_t_in
        self.G_out_t_in = G_out_t_in
        self.n_razb = n_razb
        self.mode = mode

        self.__A__ = np.zeros([4*n_razb, 4*n_razb])
        self.__b__ = np.zeros(4*n_razb)

        self.F_he_in_t = np.full(n_razb, geometry["F_he_in_t"]/n_razb)
        self.F_he_out_t = np.full(n_razb, geometry["F_he_out_t"]/n_razb)

        self.L_t = np.full(n_razb, geometry["L_t"]/n_razb)
        
        self.subst_in_t = 1 # H2O
        self.subst_out_t = 1 # H2O

        self.Tf_f_in_t = np.full(n_razb+1, T_in_t_in)
        self.Tf_in_t = np.full(n_razb, T_in_t_in)
        self.Tf_f_out_t = np.full(n_razb+1, T_out_t_in)
        self.Tf_out_t = np.full(n_razb, T_out_t_in)
        
        self.Tw_in_t = np.full(n_razb, T_in_t_in)
        self.Tw_out_t = np.full(n_razb, T_out_t_in)

        self.P_in_t = np.full(n_razb, P_in_t_in)
        self.P_out_t = np.full(n_razb, P_out_t_in)

        self.Pr_f_in_t = np.full(n_razb, rgp.rgpPRANDTLEPT(self.subst_in_t, P_in_t_in,T_in_t_in))
        self.Pr_f_out_t = np.full(n_razb, rgp.rgpPRANDTLEPT(self.subst_out_t, P_out_t_in,T_out_t_in))

        self.lambda_f_in_t = np.full(n_razb, rgp.rgpTHERMCONDPT(self.subst_in_t, P_in_t_in,T_in_t_in))
        self.lambda_f_out_t = np.full(n_razb, rgp.rgpTHERMCONDPT(self.subst_out_t, P_out_t_in,T_out_t_in))
        
        self.Pr_w_in_t = self.Pr_f_in_t
        self.Pr_w_out_t = self.Pr_f_out_t

        self.Cp_in_t = np.full(n_razb, rgp.rgpCPPT(self.subst_in_t, P_in_t_in, T_in_t_in))
        self.Cp_out_t = np.full(n_razb, rgp.rgpCPPT(self.subst_out_t, P_out_t_in, T_out_t_in))
        
        self.D_in_t = np.full(n_razb, rgp.rgpDPT(self.subst_in_t, P_in_t_in, T_in_t_in))
        self.D_out_t = np.full(n_razb, rgp.rgpDPT(self.subst_out_t, P_out_t_in, T_out_t_in))

        self.ALW_in_t = np.full(n_razb, alw_in_t)
        self.ALW_out_t = np.full(n_razb, alw_out_t)

        u_in = G_in_t_in*rgp.rgpVPT(self.subst_in_t, P_in_t_in, T_in_t_in)/geometry["F_in_t"]
        u_out = G_out_t_in*rgp.rgpVPT(self.subst_out_t, P_out_t_in, T_out_t_in)/geometry["F_out_t"]
        self.u_in_t = np.full(n_razb, u_in)
        self.u_out_t = np.full(n_razb, u_out)
        
        self.Re_in_t = np.full(n_razb, u_in*geometry["d_in_t"]/rgp.rgpKINVISPT(self.subst_in_t, P_in_t_in, T_in_t_in))
        self.Re_out_t = np.full(n_razb, u_out*geometry["d_out_t"]/rgp.rgpKINVISPT(self.subst_out_t, P_out_t_in, T_out_t_in))

        self.Q_in_t = np.zeros(n_razb)
        self.Q_out_t = np.zeros(n_razb)

        self.Q_he_in_t = 0.
        self.Q_he_out_t = 0.

        self.__Xi__ = 2*pi*self.lambda_w/log(self.geometry["d_out_t"]/self.geometry["d_in_t"])
    
    def __linearize__(self):
        """
        Линеаризация уравнений сохранения энергии и построение матриц коэффициентов __A__ and __b__
        """
        for i in range(self.n_razb):
            # уравнения (1) для ячеек
            if(i == 0): 
                # противоток
                self.__A__[i,i] = -(self.ALW_in_t[i]*self.F_he_in_t[i]*0.5 + self.G_in_t_in*self.Cp_in_t[i])
                self.__b__[i] = -(self.G_in_t_in*self.Cp_in_t[i] - self.ALW_in_t[i]*self.F_he_in_t[i]*0.5)*self.T_in_t_in
            if(i != 0):
                self.__A__[i,i-1] = self.G_in_t_in*self.Cp_in_t[i] - self.ALW_in_t[i]*self.F_he_in_t[i]*0.5
                self.__A__[i,i] = -(self.ALW_in_t[i]*self.F_he_in_t[i]*0.5 + self.G_in_t_in*self.Cp_in_t[i])
                self.__b__[i] = 0.
            self.__A__[i,i+2*self.n_razb] = self.ALW_in_t[i]*self.F_he_in_t[i]

        for i in range(self.n_razb):
            if self.mode == 1:
                # противоток
                # уравнения (2) для ячеек (противоток)
                if(i == self.n_razb-1):
                    # противоток
                    self.__A__[i+self.n_razb,i+self.n_razb] = self.G_out_t_in*self.Cp_out_t[i] + self.ALW_out_t[i]*self.F_he_out_t[i]*0.5
                    self.__b__[i+self.n_razb] = -(self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 - self.G_out_t_in*self.Cp_out_t[i])*self.T_out_t_in
                if(i != self.n_razb-1):
                    self.__A__[i+self.n_razb,i+self.n_razb] = self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 + self.G_out_t_in*self.Cp_out_t[i]
                    self.__A__[i+self.n_razb,i+self.n_razb+1] = self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 - self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+self.n_razb] = 0.
            if self.mode == 0:
                # прямоток
                # уравнения (6) для ячеек (прямоток)
                if(i == 0):
                    # прямоток
                    self.__A__[i+self.n_razb,i+self.n_razb] = self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 + self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+self.n_razb] = -(self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 - self.G_out_t_in*self.Cp_out_t[i])*self.T_out_t_in
                if(i != 0):
                    self.__A__[i+self.n_razb,i+self.n_razb-1] = self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 - self.G_out_t_in*self.Cp_out_t[i]
                    self.__A__[i+self.n_razb,i+self.n_razb] = self.ALW_out_t[i]*self.F_he_out_t[i]*0.5 + self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+self.n_razb] = 0.
            self.__A__[i+self.n_razb,i+3*self.n_razb] = -self.ALW_out_t[i]*self.F_he_out_t[i]
                
        for i in range(self.n_razb):
            # уравнения (3) для ячеек
            if(i == 0): 
                # противоток
                self.__A__[i+2*self.n_razb,i] = -self.G_in_t_in*self.Cp_in_t[i]
                self.__b__[i+2*self.n_razb] = -self.G_in_t_in*self.Cp_in_t[i]*self.T_in_t_in

            if(i != 0):
                self.__A__[i+2*self.n_razb,i] = -self.G_in_t_in*self.Cp_in_t[i]
                self.__A__[i+2*self.n_razb,i-1] = self.G_in_t_in*self.Cp_in_t[i]
                self.__b__[i+2*self.n_razb] = 0.

            self.__A__[i+2*self.n_razb,i+2*self.n_razb] = -self.__Xi__*self.L_t[i]*self.geometry["n_t"]
            self.__A__[i+2*self.n_razb,i+3*self.n_razb] = self.__Xi__*self.L_t[i]*self.geometry["n_t"]

        for i in range(self.n_razb):
            if self.mode == 1:
                # противоток
                # уравнения (4) для ячеек
                if(i == self.n_razb-1): 
                    # противоток
                    self.__A__[i+3*self.n_razb,i+self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+3*self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]*self.T_out_t_in

                if(i != self.n_razb-1):
                    self.__A__[i+3*self.n_razb,i+self.n_razb+1] = -self.G_out_t_in*self.Cp_out_t[i]
                    self.__A__[i+3*self.n_razb,i+self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+3*self.n_razb] = 0.
            if self.mode == 0:
                # прямоток
                # уравнения (8) для ячеек
                if(i == 0): 
                    # прямоток
                    self.__A__[i+3*self.n_razb,i+self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+3*self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]*self.T_out_t_in

                if(i != 0):
                    self.__A__[i+3*self.n_razb,i+self.n_razb] = self.G_out_t_in*self.Cp_out_t[i]
                    self.__A__[i+3*self.n_razb,i+self.n_razb-1] = -self.G_out_t_in*self.Cp_out_t[i]
                    self.__b__[i+3*self.n_razb] = 0.

            self.__A__[i+3*self.n_razb,i+2*self.n_razb] = -self.__Xi__*self.L_t[i]*self.geometry["n_t"]
            self.__A__[i+3*self.n_razb,i+3*self.n_razb] = self.__Xi__*self.L_t[i]*self.geometry["n_t"]


    def __calcstep__(self):
        """
        Решение СЛАУ для нахождения температур по участкам. Пересчет величин, зависящих от температур
        """

        self.__linearize__()
        results = linalg.solve(self.__A__, self.__b__)

        # обновление температур
        self.Tf_f_in_t = np.concatenate((np.array([self.T_in_t_in]), results[0:self.n_razb]), axis=0)
        if self.mode == 1:
            # противоток
            self.Tf_f_out_t = np.concatenate((results[self.n_razb:2*self.n_razb], np.array([self.T_out_t_in])), axis=0)
        if self.mode == 0:
            # прямоток
            self.Tf_f_out_t = np.concatenate((np.array([self.T_out_t_in]), results[self.n_razb:2*self.n_razb]), axis=0)
        self.Tw_in_t = results[2*self.n_razb:3*self.n_razb]
        self.Tw_out_t = results[3*self.n_razb:4*self.n_razb]

        for i in range(1,self.n_razb+1):
                self.Tf_in_t[i-1] = 0.5*(self.Tf_f_in_t[i]+self.Tf_f_in_t[i-1])
                self.Tf_out_t[i-1] = 0.5*(self.Tf_f_out_t[i]+self.Tf_f_out_t[i-1])

        # print(self.Tf_in_t)
        # print(self.Tw_in_t)
        # print(self.Tw_out_t)
        # print(self.Tf_out_t)

        # обновление зависимых величин
        for i in range(self.n_razb):
            self.Cp_in_t[i] = rgp.rgpCPPT(self.subst_in_t, self.P_in_t[i], self.Tf_in_t[i])
            self.Cp_out_t[i] = rgp.rgpCPPT(self.subst_out_t, self.P_out_t[i], self.Tf_out_t[i])

            self.D_in_t[i] = rgp.rgpDPT(self.subst_in_t, self.P_in_t[i], self.Tf_in_t[i])
            self.D_out_t[i] = rgp.rgpDPT(self.subst_out_t, self.P_out_t[i], self.Tf_out_t[i])

            self.Pr_f_in_t[i] = rgp.rgpPRANDTLEPT(self.subst_in_t, self.P_in_t[i], self.Tf_in_t[i])
            self.Pr_f_out_t[i] = rgp.rgpPRANDTLEPT(self.subst_out_t, self.P_out_t[i], self.Tf_out_t[i])
            
            self.lambda_f_in_t[i] = rgp.rgpTHERMCONDPT(self.subst_in_t, self.P_in_t[i], self.Tf_in_t[i])
            self.lambda_f_out_t[i] = rgp.rgpTHERMCONDPT(self.subst_out_t, self.P_out_t[i], self.Tf_out_t[i])

            self.Pr_w_in_t[i] = rgp.rgpPRANDTLEPT(self.subst_in_t, self.P_in_t[i], self.Tw_in_t[i])
            self.Pr_w_out_t[i] = rgp.rgpPRANDTLEPT(self.subst_out_t, self.P_out_t[i], self.Tw_out_t[i])

            self.u_in_t[i] = self.G_in_t_in*(1./self.D_in_t[i])/self.geometry["F_in_t"]
            self.u_out_t[i] = self.G_out_t_in*(1./self.D_out_t[i])/self.geometry["F_out_t"]
        
            self.Re_in_t[i] = self.u_in_t[i]*self.geometry["d_in_t"]/rgp.rgpKINVISPT(self.subst_in_t, self.P_in_t[i],self.Tf_in_t[i])
            self.Re_out_t[i] = self.u_out_t[i]*self.geometry["d_out_t"]/rgp.rgpKINVISPT(self.subst_out_t, self.P_out_t[i],self.Tf_out_t[i])

            self.ALW_in_t[i] = (self.lambda_f_in_t[i]/self.geometry["d_in_t"])*self.coil_Nu_in_t_rev(
                self.geometry["d_in_t"], 
                self.geometry["D_avg"], 
                self.Re_in_t[i],
                self.Pr_f_in_t[i],
                self.Pr_w_in_t[i],
                self.Tf_f_in_t[-1]-self.Tf_f_in_t[0])
            
            self.Q_in_t[i] = self.G_in_t_in*self.Cp_in_t[i]*abs(self.Tf_f_in_t[i]-self.Tf_f_in_t[i+1])
            self.Q_out_t[i] = self.G_out_t_in*self.Cp_out_t[i]*abs(self.Tf_f_out_t[i]-self.Tf_f_out_t[i+1])
            # self.Q_in_t[i] = abs(self.ALW_in_t[i]*self.F_he_in_t[i]*(self.Tw_in_t[i] - self.Tf_f_in_t[i]))
            # self.Q_out_t[i] = abs(self.ALW_out_t[i]*self.F_he_out_t[i]*(self.Tw_out_t[i] - self.Tf_f_out_t[i]))
            
            self.ALW_out_t[i] = (self.lambda_f_out_t[i]/self.geometry["d_out_t"])*self.coil_Nu_out_t_rev(
                self.Re_out_t[i],
                self.Pr_f_out_t[i],
                self.geometry["a_avg"],
                self.geometry["n_ryad_vert"]
            )

        self.Q_he_in_t = np.sum(self.Q_in_t)
        self.Q_he_out_t = np.sum(self.Q_out_t)


    def evaluate(self):
        Err = 1.
        while Err > 0.001:
            Ql = self.Q_he_out_t
            self.__calcstep__()
            Qn = self.Q_he_out_t

            Err = abs(Ql-Qn)/Qn
    

    def coil_Nu_out_t_rev(self, Re: float, Pr: float, a: float, n_cols: int):
        """
        Критерий Нуссельта по межтрубному пространству (обтекание змеевикового пучка труб РТМ 108.031.05-84)
                
        Arguments
        ----------
        Re (float): Критерий Рейнольдса
        Pr (float): Критерий Прандтля
        a (float): Угол набегания потока (угол навивки змеевиков) [град]
        n_cols (int): Число поперечно обтекаемых рядов
        """

        Re = abs(Re)

        if ((0. < Re) and (Re <= 40.)):
            c = 0.9
            n = 0.4
        if ((40. < Re) and (Re <= 1000.)):
            c = 0.52
            n = 0.5
        if ((1000. < Re) and (Re <= 2.e5)):
            c = 0.26
            n = 0.63
        if (2.e5 < Re):
            c = 0.02
            n = 0.84
        
        Nu0 = c*(Re**n)*(Pr**0.36)

        Cz = np.interp(
            n_cols,
            [
                0.81369322,
                1.0796577,
                1.5536537,
                2.3304806,
                3.4127716,
                4.8136932,
                6.198815,
                8.2843976,
                11.620803,
                13.877551,
                18.541145,
            ],
            [
                0.67142857,
                0.71997354,
                0.77896825,
                0.83902116,
                0.88095238,
                0.91798942,
                0.94179894,
                0.96560847,
                0.98756614,
                0.99801587,
                1,
            ])
        
        Cf = sqrt(sin(radians(a)))

        Nu = Nu0*Cz*Cf

        return Nu

    def coil_Nu_in_t_rev(self, d: float, D: float, Re: float, Pr_f: float, Pr_w: float, dT: float):
        """
        Критерий Нуссельта для течения внутри змеевиков (РТМ 108.031.05-84)

        Arguments
        ----------
        d (float): Внутренний диаметр змеевиков [м]
        D (float): Диаметр гиба змеевиков [м]
        Re (float): Критерий Рейнольдса
        Pr_f (float): Критерий Прандтля при температуре жидкости
        Pr_w (float): Критерий Прандтля при температуре стенки
        dT (float): Признак режима теплообмена (при dT > 0 считается, что теплоноситель в трубах нагревается, а при dT > 0 - что охлаждается)
        """

        Re = abs(Re)

        Re_cr = 2.e4*(d/D)**0.32
        Dn = Re*sqrt(d/D)

        if (Re < Re_cr):
            Nu0 = 0.15*(Re**0.33)*(Pr_f**0.43)*(Pr_f/Pr_w)**0.25
            if (Dn <= 11.6):
                C = 1.
            else:
                C = 0.4*Dn**0.37
        else:
            Nu0 = (0.023*Pr_f*Re**0.8)/(1+2.14*(Re**-0.1)*((Pr_f**0.7)-1.))
            if (dT > 0.):
                # нагревание теплоносителя
                C = 1 + 6.3*(1-d/D)*(d/D)**1.15
            else:
                # охлаждение теплоносителя
                C = 1 - 0.3 * exp(-0.015*d/D)
        
        Nu = C*Nu0

        return Nu

