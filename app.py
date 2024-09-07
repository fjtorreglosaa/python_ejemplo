import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

from utilidades.coordenadas import Coordenadas
from utilidades.velocidad import Velocidad

# Valores iniciales
caudal = 0.1 # m^3/s
area_inicio_tunel = 1.05 * 2.1 # m^2
area_final_tunel = 0.4 * 0.8 # m^2

# Calculos para velocidades
velocidad_entrada = caudal / area_inicio_tunel
velocidad_salida = caudal / area_final_tunel

# Se crea una lista sin elementos, para luego llenarla con coordenadas
coordenadas = []

# Toma la información del archivo data.txt y agrega cada dato a la lista de coordenadas
with open('./data.txt', 'r') as data:
    for linea in data:
        valor = linea.split(',')
        x = int(valor[0])
        y = int(valor[1])
        coordenadas.append(Coordenadas(x, y))
        
velocidades = Velocidad.obtener_velocidades(coordenadas, caudal)

# Ingresar los datos de prueba        
xi_vals = [coord.x for coord in coordenadas]
fxi_vals = [coord.y for coord in coordenadas]

# Alimentar el vector X y Y
Xi = np.array(xi_vals)
FXi = np.array(fxi_vals)

# Configuración de la tabla con los valores
numero_pares_ordenados = len(FXi)
ki = np.arange(0, numero_pares_ordenados, 1)
tabla_de_valores = np.concatenate(([ki], [Xi], [FXi]), axis = 0)
tabla_de_valores = np.transpose(tabla_de_valores)

# Calculo de la tabla de diferencias finitas
tabla_de_diferencias_finitas = np.zeros((numero_pares_ordenados, numero_pares_ordenados), dtype = float)
tabla_de_valores = np.concatenate((tabla_de_valores, tabla_de_diferencias_finitas), axis = 1)

[filas, columnas] = np.shape(tabla_de_valores)
diagonal = filas - 1

j = 3
while ( j < columnas):
    i = 0
    while (i < diagonal):
        tabla_de_valores[i, j] = tabla_de_valores[i + 1, j - 1] - tabla_de_valores[i, j - 1]
        i = i + 1
    j = j + 1
    diagonal = diagonal - 1
    
# Calculo del polinomio de diferencias finitas
n = len(Xi)
x = sym.Symbol('x')
diferencia_finita = tabla_de_valores[0,3:]
h = Xi[1] - Xi[0]
polinomio = FXi[0]

j = 1
grado_polinomio = 50
for j in range(0, min(n, grado_polinomio)):
    denominador = math.factorial(j)*(h**j)
    factor = diferencia_finita[j - 1]/denominador
    termino = 1
    for k in range(0, j, 1):
        termino = termino * (x - Xi[k])
    polinomio = polinomio + termino * factor

polinomio_simple = sym.expand(polinomio)

px = sym.lambdify(x, polinomio_simple)

print(polinomio)

muestras = 50
a = np.min(Xi)
b = np.max(Xi)
p_xi = np.linspace(a, b, muestras)
pxi = px(p_xi)

# Gráfica de velocidad

plt.plot(Xi, FXi, 'o', label = 'Puntos')
plt.plot(p_xi, pxi, label = 'polinomio')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Campo Vectorial (u, v)')
plt.grid()
plt.show()
