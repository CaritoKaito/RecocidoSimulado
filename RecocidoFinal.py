import random
import math
#import matplotlib.pyplot as plt

#función que quiero optimizar
def funcion(x):
    return x**2

#valores inciales
temp_inicial = 100
tasa_enfriamiento = 0.9
solucion_actual = 10
iteraciones = 1000

#funcion recocido simulado
def recocido_simulado(temp_inicial, tasa_enfriamiento, solucion_actual, iteraciones):

    temperatura = temp_inicial
    solucion_mejor = solucion_actual
    mejores_soluciones = funcion(solucion_actual)
    i = 0

    # Se detiene cuando se enfria lo suficiente (NO muy alta, No muy baja)
    while temperatura > 0.1 and i < iteraciones:
        #Explorar diferenctes soluciones
        solucion_nueva = solucion_actual + random.uniform(-1, 1)
        #compara soluciones
        delta = funcion(solucion_nueva) - funcion(solucion_actual)
        #Delta es mejor
        if delta < 0:
            solucion_actual = solucion_nueva
            #Mejores soliciones
            if funcion(solucion_nueva) < mejores_soluciones:
                solucion_mejor = solucion_nueva
                mejores_soluciones = funcion(solucion_nueva)
        #Delta es peor
        else:
            #determinar si la nueva solución peor se acepta o no. 
            p = math.exp(-delta / temperatura)
            # Mucho Peor o poco peor
            if random.uniform(0, 1) < p:
                solucion_actual = solucion_nueva
        
        #reducimos la temperatura | sumamos i + 1 en cada iteracio             
        temperatura *= tasa_enfriamiento
        i += 1
    return solucion_mejor

#El resultado devuelto es la solución optimizada encontrada por el algoritmo.
resultado = recocido_simulado(temp_inicial, tasa_enfriamiento, solucion_actual, iteraciones)
print("Mejor solución optimizada:", resultado)

#########################################
## Codigo que supuestamente Grafica    ##
#########################################

# import random
# import math
# import matplotlib.pyplot as plt

# #función que quiero optimizar
# def funcion(x):
#     return x**2

# #valores inciales
# temp_inicial = 100
# tasa_enfriamiento = 0.9
# solucion_actual = 10
# iteraciones = 1000

# #funcion recocido simulado
# def recocido_simulado(temp_inicial, tasa_enfriamiento, solucion_actual, iteraciones):

#     temperatura = temp_inicial
#     solucion_mejor = solucion_actual
#     mejores_soluciones = funcion(solucion_actual)
#     i = 0
#     soluciones = [solucion_actual]

#     # Se detiene cuando se enfria lo suficiente (NO muy alta, No muy baja)
#     while temperatura > 0.1 and i < iteraciones:
#         #Explorar diferenctes soluciones
#         solucion_nueva = solucion_actual + random.uniform(-1, 1)
#         #compara soluciones
#         delta = funcion(solucion_nueva) - funcion(solucion_actual)
#         #Delta es mejor
#         if delta < 0:
#             solucion_actual = solucion_nueva
#             #Mejores soliciones
#             if funcion(solucion_nueva) < mejores_soluciones:
#                 solucion_mejor = solucion_nueva
#                 mejores_soluciones = funcion(solucion_nueva)
#         #Delta es peor
#         else:
#             #determinar si la nueva solución peor se acepta o no. 
#             p = math.exp(-delta / temperatura)
#             # Mucho Peor o poco peor
#             if random.uniform(0, 1) < p:
#                 solucion_actual = solucion_nueva
        
#         #reducimos la temperatura | sumamos i + 1 en cada iteracio             
#         temperatura *= tasa_enfriamiento
#         i += 1
#         soluciones.append(solucion_actual)
#     return solucion_mejor, soluciones

# #El resultado devuelto es la solución optimizada encontrada por el algoritmo.
# resultado, soluciones = recocido_simulado(temp_inicial, tasa_enfriamiento, solucion_actual, iteraciones)
# print("Mejor solución optimizada:", resultado)

# x = [i for i in range(len(soluciones))]
# y = soluciones
# plt.plot(x, y)
# plt.show()