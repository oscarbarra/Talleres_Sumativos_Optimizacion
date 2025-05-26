
from sympy import sympify
from numpy import linspace,pi
from grafico import crea_grafico

def valor_funcion_pivote(fun,lmd,valores_x,i):
    valor_xa = {"x":valores_x[i-1]}
    valor_xb = {"x":valores_x[i]}
    fxa = sympify(fun).subs(valor_xa)
    fxb = sympify(fun).subs(valor_xb)
    evaluacion = lmd*fxa + (1-lmd)*fxb
    return evaluacion

def valor_funcion_original_con_lambda(fun,lmd,valores_x,i):
    valor_xa = valores_x[i-1]
    valor_xb = valores_x[i]
    valor_xf = {"x":lmd*valor_xa + (1-lmd)*valor_xb}
    evaluacion = sympify(fun).subs(valor_xf)
    return evaluacion

def es_concava(fun,valores_lmd,valores_x):
    for lmd in valores_lmd:
        for i in range(1, len(valores_x)):
            valor_pivote = valor_funcion_pivote(fun,lmd,valores_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun,lmd,valores_x,i)
            restriccion_concavidad = valor_fun_org_lmd >= valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def es_concava_estricta(fun,valores_lmd,valores_x):
    for lmd in valores_lmd:
        for i in range(1, len(valores_x)):
            valor_pivote = valor_funcion_pivote(fun,lmd,valores_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun,lmd,valores_x,i)
            restriccion_concavidad = valor_fun_org_lmd > valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def es_convexa(fun,valores_lmd,valores_x):
    for lmd in valores_lmd:
        for i in range(1, len(valores_x)):
            valor_pivote = valor_funcion_pivote(fun,lmd,valores_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun,lmd,valores_x,i)
            restriccion_concavidad = valor_fun_org_lmd <= valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def es_convexa_estricta(fun,valores_lmd,valores_x):
    for lmd in valores_lmd:
        for i in range(1, len(valores_x)):
            valor_pivote = valor_funcion_pivote(fun,lmd,valores_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun,lmd,valores_x,i)
            restriccion_concavidad = valor_fun_org_lmd < valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def evaluar_convexidad_y_concavidad(obj,fun,valores_lmd,valores_x):
    objetivos_validos = ("convexa", "convexa estricta", "concava", "concava estricta")

    if obj not in objetivos_validos:
        mensaje = f"Porfavor ingresar un objetivo valido: {objetivos_validos}"
        return mensaje
    
    evaluacion = None
    if obj == "concava":
        evaluacion = es_concava(fun,valores_lmd,valores_x)
    elif obj == "convexa":
        evaluacion = es_convexa(fun,valores_lmd,valores_x)
    elif obj == "concava estricta":
        evaluacion = es_concava_estricta(fun,valores_lmd,valores_x)
    elif obj == "convexa estricta":
        evaluacion = es_convexa_estricta(fun,valores_lmd,valores_x)
    cumple = "Sí" if evaluacion else "No"
    intervalo = f"[{valores_x[0]:.2f}, {valores_x[-1]:.2f}]"
    mensaje = f"La función {fun} {cumple} es {obj} en el intervalo {intervalo}"
    return mensaje

def main():
    # Objetivo de la evaluación
    obj = "convexa"
    # Función a la que se le determinará si es concava o conexa
    fun = "(x -1.5)**2 + 0.5"
    # Valor de Lambda
    valores_lmd = linspace(0,1,20)
    # Rando de evaluación
    valores_x = linspace(0.5, 2.0, 100)
    # Resultado de la evalución
    resultado = evaluar_convexidad_y_concavidad(obj,fun,valores_lmd,valores_x)
    # Muestra el resultado en consola
    print(resultado)
    # Muestra un grafico con los resultados
    crea_grafico(fun,valores_x,valores_lmd,resultado)
    return

if __name__ == "__main__":
    main()