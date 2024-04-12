import math

# ЗАДАЕМ ОСНОВНЫЕ ПЕРЕМЕННЫЕ

# Входные параметры змеевика
S_ob = 20000. # Первое приблежение теплообменной площади
H_nav_zm_teor = 1000 # Первое приближение активной высоты навивки 
d_trubki_nar = 14. # Наружный диаметр трубки
d_trubki_vn = 11. # Внутренний диаметр трубки
m_trubok = 36 # Первое приблежение общего количества трубок
n_ryadov = 6 # Первое прибдежение количества рядов навивки
S1_schag_gor = 17. # Горизонтальный шаг змеевика
S2_schag_vert = 17. # Вертикальный шаг змеевика
D_nav_zm_1 = 400. # Первое приближение диаметра первого ряда змеевика
pi = math.pi # Число пи чтоб не ебаться с женщинами

# Параметры трубной доски

n_tr_dosk = 3 # Количество рядов отверстий в трубной доске
# НАДО ИХ РАСПРЕДЕЛИТЬ ПО РЯДАМ и задать им диаметры

m_tr_dosk_1 = 12 # Количество отверстий в первом ряду трубной доски
m_tr_dosk_2 = 12 # Количество отверстий во втором ряду трубной доски
m_tr_dosk_3 = 12 # Количество отверстий в третьем ряду трубной доски
D_zad_tr_1 = 400 # Диаметр первого ряда заделки в трубной доске
D_zad_tr_2 = 450 # Диаметр второго ряда заделки в трубной доске
D_zad_tr_3 = 500 # Диаметр третьего ряда заделки в трубной доске
l_okr_sekt = pi*D_nav_zm_1/m_tr_dosk_1 # Длина окружности между началами отгибок соседних трубок
n_zm_akt = 1 # Порядковый номер активного змеевика в ряду навивки

# Объявляем переменные для формирования массива

n_ryad = []
D_ryad = []
K_otn_D = []
Z_teor = [] 
Z_deystv = []
n_ob_zm = []
n_ob_zm_teor = []
A_nav = [] 
l_zm = []
l_zm_summ = []
H_nav_zm = []

# Считается каждый ряд отдельно

# РАСЧЕТ ТРУБНОЙ СИСТЕМЫ
Z_sredn=m_trubok/n_ryadov # Средняя заходность
D_sredn=((D_nav_zm_1+n_ryadov*S1_schag_gor)+D_nav_zm_1)/2 # Средний диаметр навивки
b_zazor=((D_nav_zm_1+n_ryadov*S1_schag_gor)-D_nav_zm_1)/2 # Ширина кольцевого зазора

for i in range(n_ryadov):

    n_ryad.append(i) # Порядковый номер ряда навивки (1 ряд = 0 ряд)
    
    D_ryad.append(D_nav_zm_1+S1_schag_gor*2*n_ryad[i]) # Диаметр ряда навивки
    K_otn_D.append(D_sredn/D_ryad[i]) # Отношение для определения заходности
    Z_teor.append(Z_sredn/K_otn_D[i]) # Теоретическая заходность для ряда i
    Z_deystv.append(math.ceil(Z_teor[i])) # Фактическая заходность для ряда i
    A_nav.append((math.atan(S2_schag_vert*Z_deystv[i]/pi*D_ryad[i]))*180/pi) # Угол навивки змеевика в пересчете на значение угла
    n_ob_zm_teor.append(H_nav_zm_teor/S2_schag_vert*Z_deystv[i]) # Число оборотов змеевика в ряду теоретическое
    n_ob_zm.append(math.ceil(n_ob_zm_teor[i])) # Фактическое число оборотов змеевика в ряду
    H_nav_zm.append(Z_deystv[i]*n_ryad[i]) # Фактическая высота навивики ряда змеевика
    l_zm.append(pi*D_ryad[i]*n_ob_zm[i]/math.cos(A_nav[i])) # Длина змеевика в ряду навивки
    l_zm_summ.append(l_zm[i]*Z_deystv[i])  # Общая длинна змеевиков в ряду навивки
    print(n_ryad)
    print(H_nav_zm)

    

# class Zmeevik:
#     init(self):
#         self.var1 = 0
#         self.var3 = 0
#         self.var3 = 0 
# [23:35]
# Zmeevik zm
# print(zm.var1)

    
# print("xyi")
# for j in range(m_tr_dosk_1):
#     xyi[j]
# B # Угол между точками заделки концов трубы в нижнюю и в верхнюю трубные доски
# D_otg_verh # 
# D_otg_niz #
# H_schag_zm #
# H_gab #
# H_ob=1000 #"мм" "Общая высота"
# D=100 #"мм" "Диаметр"0
# A=math.atan(h/2) #Угол подьема


# Расчет геометрии змеевика
# расчета необходимой площади
# расчета рядов в теплообменной поверхности
# отгибки из трубных досок

# Расчет теплогидравлический
# сказал типа ок ему или нет
 
# и выдал данные в NX или компасе