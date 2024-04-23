from coil_he import CoilHE
import matplotlib.pyplot as plt
import numpy as np

# Исследование режимов работы теплообменнике

rec_detail = CoilHE(
    18.,
    40.+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    5*1.667,
    5*1.667,
    6,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.e-3,
        "s_vert": 17.e-3,
        "n_ryad_vert": 50,
        "a_avg": 4.,
        "D_avg": 0.25,
        "L_t": 12.45,
        "n_t": 44,
        "F_he_in_t": 22.283,
        "F_he_out_t": 28.752,
        "F_in_t": 0.0053135642,
        "F_out_t": 0.009319
    }
)

rec_avg = CoilHE(
    18.,
    40.+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    5*1.667,
    5*1.667,
    1,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.e-3,
        "s_vert": 17.e-3,
        "n_ryad_vert": 50,
        "a_avg": 4.,
        "D_avg": 0.25,
        "L_t": 12.45,
        "n_t": 44,
        "F_he_in_t": 22.283,
        "F_he_out_t": 28.752,
        "F_in_t": 0.0053135642,
        "F_out_t": 0.009319
    }
)

rec_detail.evaluate()
rec_avg.evaluate()

print("Total power (5 sections) "+str(rec_detail.Q_he_in_t*1.e-3)+" kWt")
print("Total power (1 sections) "+str(rec_avg.Q_he_in_t*1.e-3)+" kWt")
print("")
plt.plot(rec_detail.ALW_in_t)
plt.plot(np.full(6, rec_avg.ALW_in_t))
plt.plot(
    [
        1.060606053E+04,
        1.185548805E+04,
        1.291420867E+04,
        1.376570408E+04,
        1.441472457E+04,
        1.489972933E+04
    ]
)
plt.xlabel("участки")
plt.ylabel("Коэффициент теплоотдачи, Вт/(м2*К)")
plt.legend(["Нагреваемый (5 участков, внутритрубное пространство)",
           "Нагреваемый (1 участок, внутритрубное пространство)", "КОРСАР"])
plt.show()
