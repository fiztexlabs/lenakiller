from coil_he import CoilHE
import matplotlib.pyplot as plt


rec = CoilHE(
    18.,
    40.+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    1.667,
    1.667,
    100,
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


rec.evaluate()

print("Total power "+str(rec.Q_he_in_t*1.e-3)+" kWt")
print("")
plt.plot(rec.Tf_in_t - 273.15)
plt.plot(rec.Tf_out_t - 273.15)
plt.xlabel("участки")
plt.ylabel("Температура, C")
plt.legend(["Внутритрубное пространство", "Межтрубное пространство"])
plt.show()
