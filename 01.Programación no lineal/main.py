
import numpy as np
from grafico import graficar

def evaluar_restricciones(x1,x2,b,A,signs):
    puntos_factibles = list()
    cumple = True
    # i: cantidad de restricciones | idice de las filas de A
    for i in range(A.shape[0]):
        # Valor de la restricción
        factible = A[i,0]*x1 + A[i,1]*x2
        # Evalua las resticciones de menor igual que
        if signs[i] == "<=" and not (factible <= b[i]):
            cumple = False
        # Evalua las restricciones de mayor igual que
        elif signs[i] == ">=" and not (factible >= b[i]):
            cumple = False
    # Si cumple todas las restricciones se guarda como un punto factible
    if cumple:
        puntos_factibles.append([x1,x2])
    return puntos_factibles

def encuentra_puntos_factibles(rango_x1,rango_x2,b,A,signs):
    puntos_factibles = list()
    # x1: toma todos los valores dentro de un rango
    for x1 in rango_x1:
        # x2: toma todos los valores dentro de un rango
        for x2 in rango_x2:
            # Guarda todos los puntos que cumplan todas las restriciones
            puntos_factibles += evaluar_restricciones(x1,x2,b,A,signs) 
    return np.array(puntos_factibles)

def evaluar_parte_lineal(p,z):
    parte_lineal = list()
    # Guarda el valor de la combinación lineal
    evalucion = 0
    # Indice de la variable que entra
    idx = 0
    # Realiza la combinación lineal
    for coef in z:
        suma = coef*p[idx]
        evalucion += suma
        idx += 1
    parte_lineal.append(evalucion)
    return parte_lineal

def evaluar_parte_no_lineal(p,znl):
    parte_no_lineal = list()
    # Guarda el valor de las operaciones no lineales
    evaluacion = 0
    # Indice de la variables que entra
    idx = 0
    # Realiza las operaciones no lineales
    for coef in znl:
        suma = 0
        # Revisa si existe alguna operación multiple | (coef1*x1 + coef2*x2)
        if isinstance(coef, (list, tuple)):
            suma = coef[0]*p[0] + coef[1]*p[1]
            evaluacion += suma**2
        # Evalua si es una operación unica | coef * x1
        elif isinstance(coef, (int, float)):
            suma = coef*(p[idx]**2)
            evaluacion += suma
            idx += 1
    parte_no_lineal.append(evaluacion)
    return parte_no_lineal

def evaluar_funcion_objetivo(puntos_factibles,teta,z,znl):
    parte_lineal = list()
    parte_no_lineal = list()
    # Evalua la función objetivo en partes
    for p in puntos_factibles:
        parte_lineal += evaluar_parte_lineal(p,z)
        parte_no_lineal += evaluar_parte_no_lineal(p,znl)
    # Ajuste de formato para facilitar operaciones futuras
    parte_lineal = np.array(parte_lineal)
    parte_no_lineal = np.array(parte_no_lineal)
    # Evalua la función objetivo completa
    puntos_evaluados_fobj = parte_lineal - teta*parte_no_lineal
    return puntos_evaluados_fobj 

def solucion_funcion_objetivo(puntos_factibles,puntos_evaluados_fobj,obj):
    # Inice del valor inicial de pivoteo
    idx_optimo = 0
    # Valor de inicial de pivoteo
    sol_optima = puntos_evaluados_fobj[idx_optimo]
    # Encuentra el valor maximo o minimo de la función objetivo
    for i in range(puntos_evaluados_fobj.shape[0]):
        # Valor del punto que se esta evaluando
        punto_interes = puntos_evaluados_fobj[i]
        # En caso de maximización evalua si es el punto optimo
        if obj == "max" and punto_interes > sol_optima:
            sol_optima = punto_interes
            idx_optimo = i
        # En caso de minimización evalua si es el punto optimo
        elif obj == "min" and punto_interes < sol_optima:
            sol_optima = punto_interes
            idx_optimo = i
    return (list(puntos_factibles[idx_optimo]),sol_optima)

def mostrar_resultado_obtenido(teta,solucion):
    print("-------------------------------------")
    print("Coeficiente de la cantidad de riesgo:")
    print("teta: ", teta)
    print("puntos optimos:")
    print("x1: ", solucion[0][0])
    print("x2: ", solucion[0][1])
    print("solución optima:")
    print("z: ",solucion[1])
    print("-------------------------------------")
    return

def fuerza_bruta(obj,rango_x1,rango_x2,teta,z,znl,b,A,signs):
    # Encuentra todos los puntos que cumplen las restricciones
    puntos_factibles = encuentra_puntos_factibles(rango_x1,rango_x2,b,A,signs)
    # Evalua los puntos factibles en la función objetivo
    puntos_evaluados_fobj = evaluar_funcion_objetivo(puntos_factibles,teta,z,znl)
    # Encuentra el punto optimo que maximiza o minimiza la funcion objetivo
    solucion = solucion_funcion_objetivo(puntos_factibles,puntos_evaluados_fobj,obj)
    # Muestra los resultados por consola
    mostrar_resultado_obtenido(teta,solucion)
    # Graficar el resultado
    graficar(A, b, signs, solucion, teta)
    return

def main():
    # Objetivo de la optimización
    obj = "max"
    # Angulo de evalución
    teta = 100.0
    # Rangos de evaluación
    rango_x1 = np.linspace(0,5,100) # 0 --> 5 incluyendo decimales
    rango_x2 = np.linspace(0,5,100) # 0 --> 5 incluyendo decimales
    # Función objetivo: 1.20*x1 + 1.16*x2 - teta*(2*x1² + 1*x2² + (x1 + x2)²)
    # Coeficientes lienales de la función objetivo
    z = np.array([1.20,1.16])
    # Coeficientes NO linealies de la función objetivo
    znl = np.array([2,1,(1,1)], dtype=object)
    # Restricciones del modelo
    b = np.array([5,0,0])
    # Coeficientes de las restricciones
    A = np.array([
        [1,1],
        [-1,0],
        [0,-1]
    ])
    # Singnos de las restricciones
    signs = np.array(["<=","<=","<="])
    # Solución del modelo
    fuerza_bruta(obj,rango_x1,rango_x2,teta,z,znl,b,A,signs)
    return

if __name__ == "__main__":
    main()