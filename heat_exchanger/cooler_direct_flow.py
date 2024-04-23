from coil_he import CoilHE
import matplotlib.pyplot as plt
import pandas as pd

# тестирование прямоточного режима работы теплообменника-холодильника

cooler = CoilHE(
    18.,
    40.+273.15,
    325.+273.15,
    15.7e6,
    15.7e6,
    13.889,
    3.056,
    10,
    mode = 0,
    geometry={
        "d_in_t": 12.4e-3,
        "d_out_t": 16.e-3,
        "s_hor": 17.e-3,
        "s_vert": 17.e-3,
        "n_ryad_vert": 50,
        "a_avg": 10.,
        "D_avg": 0.377,
        "L_t": 6.024,
        "n_t": 36,
        "F_he_in_t": 8.579249854,
        "F_he_out_t": 11.06999981,
        "F_in_t": 0.0053,
        "F_out_t": 0.00435
    }
)

cooler.evaluate()

print("Total power "+str(cooler.Q_he_in_t*1.e-3)+" kWt")
print("")
plt.plot(cooler.Tf_in_t - 273.15)
plt.plot(cooler.Tf_out_t - 273.15)
plt.xlabel("участки")
plt.ylabel("Температура, C")
plt.legend(["Внутритрубное пространство", "Межтрубное пространство"])
plt.show()
