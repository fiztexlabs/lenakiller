from coil_he import CoilHE
import matplotlib.pyplot as plt

cooler = CoilHE(
    18.,
    40.+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    13.889,
    3.056,
    500,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.e-3,
        "s_vert": 17.e-3,
        "n_ryad_vert": 3,
        "a_avg": 10.,
        "D_avg": 0.377,
        "F_he_in_t": 8.414,
        "F_he_out_t": 10.857,
        "F_in_t": 0.0052170858,
        "F_out_t": 0.0043474616
    }
)

cooler.evaluate()

print("Total power "+str(cooler.Q_he_in_t*1.e-3)+" kWt")
plt.plot(cooler.Tf_in_t - 273.15)
plt.plot(cooler.Tf_out_t - 273.15)
plt.xlabel("участки")
plt.ylabel("Температура, C")
plt.legend(["Внутритрубное пространство", "Межтрубное пространство"])
plt.show()
