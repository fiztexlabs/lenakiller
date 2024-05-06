from coil_he import CoilHE
import matplotlib.pyplot as plt
import numpy as np

# Исследование режимов работы теплообменнике

rec_detail = CoilHE(
    18.5,
    42.3+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    1.667,
    1.667,
    6,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.6e-3,
        "s_vert": 18.e-3,
        "n_ryad_vert": 70,
        "a_avg": 7.0127,
        "D_avg": 0.411,
        "L_t": 12.46,
        "n_t": 44,
        "F_he_in_t": 2.135709942E+01,
        "F_he_out_t": 2.755754764E+01,
        "F_in_t": 5.300000000E-03,
        "F_out_t": 9.320000000E-03
    }
)

rec_avg = CoilHE(
    18.5,
    42.3+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    1.667,
    1.667,
    1,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.e-3,
        "s_vert": 18.e-3,
        "n_ryad_vert": 70,
        "a_avg": 7.0127,
        "D_avg": 0.411,
        "L_t": 12.46,
        "n_t": 44,
        "F_he_in_t": 2.135709942E+01,
        "F_he_out_t": 2.755754764E+01,
        "F_in_t": 5.300000000E-03,
        "F_out_t": 9.320000000E-03
    }
)

rec_detail.evaluate()
rec_avg.evaluate()

print("Total power (6 sections) "+str(rec_detail.Q_he_in_t*1.e-3)+" kWt")
print("Total power (1 sections) "+str(rec_avg.Q_he_in_t*1.e-3)+" kWt")
print("")

in_t = plt.figure()
plt.plot(rec_detail.ALW_in_t)
plt.plot(np.full(6, rec_avg.ALW_in_t))
plt.plot(
    [
        2.520016105E+03,
        3.281437333E+03,
        3.972259526E+03,
        4.554041864E+03,
        5.024622278E+03,
        5.408687784E+03

    ]
)
plt.xlabel("участки")
plt.ylabel("Коэффициент теплоотдачи, Вт/(м2*К)")
plt.legend(["Нагреваемый (6 участков, внутритрубное пространство)",
           "Нагреваемый (1 участок, внутритрубное пространство)", "КОРСАР"])

out_t = plt.figure()
plt.plot(rec_detail.ALW_out_t)
plt.plot(np.full(6, rec_avg.ALW_out_t))
plt.plot(
    [
        4.892453345E+03,
        5.241146174E+03,
        5.522495165E+03,
        5.724556398E+03,
        5.854668567E+03,
        5.946906178E+03
    ]
)
plt.xlabel("участки")
plt.ylabel("Коэффициент теплоотдачи, Вт/(м2*К)")
plt.legend(["Греющий (6 участков, межтрубное пространство)",
           "Греющий (1 участок, межтрубное пространство)", "КОРСАР"])
plt.show()
