import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados de coordenadas (en mm)
x_coords = np.array([0, 16, 41, 66, 90, 115, 140, 164, 189, 214, 238, 263, 287, 312, 337, 361, 
                     386, 410, 435, 459, 484, 508, 532, 557, 581, 605, 630, 654, 678, 702, 726,
                     750, 774, 798, 822, 846, 870, 894, 917, 941, 964, 988, 1011, 1034, 1057, 
                     1080, 1103, 1126, 1148, 1171, 1193, 1215, 1237, 1259, 1280, 1301, 1322, 
                     1343, 1364, 1384, 1404, 1423, 1443, 1462, 1480, 1498, 1516, 1533, 1550, 
                     1566, 1581, 1597, 1611, 1625, 1638, 1650, 1662, 1672, 1682, 1690, 1697, 
                     1704, 1711, 1718, 1726, 1733, 1741, 1749, 1757, 1765, 1773, 1781, 1789, 
                     1797, 1806, 1814, 1822, 1830, 1839, 1847, 1856, 1864, 1872, 1889, 1898, 
                     1906, 1915, 1923, 1932, 1940, 1949, 1957, 1966, 1975, 1983, 1992, 2000, 
                     2009, 2017, 2026, 2035, 2043, 2052, 2060, 2069, 2078, 2086, 2095, 2103, 
                     2112, 2121, 2129, 2138, 2147, 2155, 2164, 2172, 2181, 2190, 2198, 2207, 
                     2216, 2224, 2233, 2241, 2250, 2259, 2267, 2276, 2285, 2293, 2302, 2310, 
                     2319, 2328, 2336, 2345, 2354, 2362, 2371, 2380, 2388, 2397, 2405, 2414, 
                     2423, 2431, 2440, 2449, 2457, 2466, 2475, 2483, 2492, 2500])
y_coords = np.array([1050, 1050, 1050, 1050, 1050, 1050, 1050, 1050, 1050, 1050, 1049, 1047, 1046, 
                     1044, 1042, 1040, 1038, 1036, 1034, 1032, 1029, 1027, 1024, 1021, 1018, 1015, 
                     1012, 1009, 1005, 1002, 998, 994, 990, 986, 982, 977, 973, 968, 963, 958, 952, 
                     947, 941, 935, 929, 923, 916, 910, 903, 895, 888, 881, 873, 865, 856, 848, 839, 
                     830, 821, 811, 801, 791, 781, 771, 760, 749, 738, 726, 715, 703, 691, 679, 667, 
                     655, 643, 630, 618, 606, 594, 582, 571, 563, 555, 548, 542, 536, 530, 525, 520, 
                     515, 510, 506, 502, 498, 494, 490, 487, 483, 480, 477, 474, 471, 468, 463, 460, 
                     458, 456, 454, 451, 449, 447, 445, 444, 442, 440, 439, 437, 435, 434, 433, 431, 
                     430, 429, 427, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 416, 416, 415, 
                     414, 413, 413, 412, 411, 411, 410, 410, 409, 408, 408, 408, 407, 407, 406, 406, 
                     405, 405, 405, 404, 404, 404, 403, 403, 403, 402, 402, 402, 402, 402, 401, 401, 
                     401, 401, 401, 401, 400, 400])

# Convertir coordenadas a metros
x_coords_m = x_coords / 1000  # mm to m
y_coords_m = y_coords / 1000  # mm to m

# Área en la entrada y salida del túnel
A_in = 1050 / 1000  # Entrada (m)
A_out = 400 / 1000  # Salida (m)

# Interpolación del área transversal a lo largo del túnel
A = np.interp(x_coords_m, [0, max(x_coords_m)], [A_in, A_out])

# Flujo constante
Q = 0.1  # m^3/s, caudal proporcionado

# Velocidades a lo largo del túnel
v = Q / A

# Cálculo de aceleración utilizando diferencias finitas manuales
# Aceleración centrada en el interior del dominio
dv = np.zeros_like(v)
for i in range(1, len(v)-1):
    dv[i] = (v[i+1] - v[i-1]) / (x_coords_m[i+1] - x_coords_m[i-1])

# Aceleración hacia adelante para el primer punto y hacia atrás para el último
dv[0] = (v[1] - v[0]) / (x_coords_m[1] - x_coords_m[0])
dv[-1] = (v[-1] - v[-2]) / (x_coords_m[-1] - x_coords_m[-2])

# Gráfica de velocidades y aceleraciones a lo largo del túnel
plt.figure(figsize=(14, 6))

# Gráfico de velocidad
plt.subplot(1, 2, 1)
plt.plot(x_coords_m, v, label="Velocidad", color="blue")
plt.xlabel("Longitud del túnel (m)")
plt.ylabel("Velocidad (m/s)")
plt.title("Distribución de velocidad a lo largo del túnel")
plt.grid(True)
plt.legend()

# Gráfico de aceleración
plt.subplot(1, 2, 2)
plt.plot(x_coords_m, dv, label="Aceleración", color="red")
plt.xlabel("Longitud del túnel (m)")
plt.ylabel("Aceleración (m/s²)")
plt.title("Distribución de aceleración a lo largo del túnel")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()