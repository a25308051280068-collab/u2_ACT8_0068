import numpy as np
import matplotlib.pyplot as plt

# Fecha = jueves/29/octubre/10/2026
# Christian Garcia Jimenez Nc = 0068
print("Christian Garcia Jimenez Nc = 0068")

# Codigo

diasX = ["lun", "mart", "mier", "jue", "vie"]
califa_VA_y = [5, 6, 3, 8, 10]
plt.bar(diasX, califa_VA_y)
plt.title("califa en VA de Chrisian Garcia Jimenez Nc = 0068")
plt.xlabel("dias semana habil 0068")
plt.ylabel("califas en VA 0068")
plt.grid()
plt.show()
