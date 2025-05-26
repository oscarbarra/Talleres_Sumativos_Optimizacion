
from numpy import linspace
from sympy import sympify

def valor_funcion_pivote(fun_original,lmd,rango_x,i):
    valor_xa = {"x":rango_x[i-1]}
    valor_xb = {"x":rango_x[i]}
    fxa = sympify(fun_original).subs(valor_xa)
    fxb = sympify(fun_original).subs(valor_xb)
    evaluacion = lmd*fxa + (1-lmd)*fxb
    return evaluacion

def valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i):
    valor_xa = rango_x[i-1]
    valor_xb = rango_x[i]
    valor_xf = {"x":lmd*valor_xa + (1-lmd)*valor_xb}
    evaluacion = sympify(fun_original).subs(valor_xf)
    return evaluacion

def es_concava(fun_original,rango_lmd,rango_x):
    for lmd in rango_lmd:
        for i in range(1, len(rango_x)):
            valor_pivote = valor_funcion_pivote(fun_original,lmd,rango_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i)
            restriccion_concavidad = valor_fun_org_lmd <= valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def es_convexa(fun_original,rango_lmd,rango_x):
    for lmd in rango_lmd:
        for i in range(1, len(rango_x)):
            valor_pivote = valor_funcion_pivote(fun_original,lmd,rango_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i)
            restriccion_concavidad = valor_fun_org_lmd >= valor_pivote
            if (not restriccion_concavidad):
                return False
    return True

def evaluar_convexidad_y_concavidad(obj,fun_original,rango_lmd,rango_x):
    objetivos_validos = ("convexa", "convexa estricta", "concava", "concava estricta")

    if obj not in objetivos_validos:
        mensaje = f"Porfavor ingresar un objetivo valido: {objetivos_validos}"
        return mensaje
    
    rango_final = rango_x[1:-2] if "estricta" in obj else rango_x
    cumple = es_concava(fun_original,rango_lmd,rango_final) if "concava" in obj else es_convexa(fun_original,rango_lmd,rango_final)
    parte_1_mensaje = "Sí" if cumple else "No"
    intervalo = f"[{rango_x[1]:.2f}, {rango_x[-2]:.2f}]" if "estricta" in obj else f"({rango_x[0]:.2f}, {rango_x[-1]:.2f})"
    mensaje = f"La función {fun_original} {parte_1_mensaje} es {obj} en el intervalo {intervalo}"
    return mensaje


def main():
    # Objetivo de la evaluación
    obj = "convexa estricta"
    # Función a la que se le determinará si es concava o conexa
    fun_original = "x^2"
    # Valor de Lambda
    rango_lmd = linspace(0,1,20)
    # Rando de evaluación
    rango_x = linspace(1, 10, 100)
    # Resultado de la evalución
    resultado = evaluar_convexidad_y_concavidad(obj,fun_original,rango_lmd,rango_x)
    # Muestra el resultado en consola
    print(resultado)
    return

if __name__ == "__main__":
    main()