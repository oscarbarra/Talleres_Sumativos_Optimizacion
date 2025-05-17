
from numpy import linspace, pi
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
      convert_xor, implicit_multiplication_application

transformaciones = standard_transformations + (convert_xor,implicit_multiplication_application)

def valor_funcion_pivote(fun_original,lmb,rango_x,i):
    valor_xa = {"X":rango_x[i-1]}
    valor_xb = {"X":rango_x[i]}
    local_dict_xa = {**valor_xa}
    local_dict_xb = {**valor_xb}
    fxa = parse_expr(fun_original, local_dict_xa, transformations=transformaciones, evaluate=True)
    fxb = parse_expr(fun_original, local_dict_xb, transformations=transformaciones, evaluate=True)
    evaluacion = lmb*fxa + (1-lmb)*fxb
    return evaluacion

def valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i):
    valor_xa = rango_x[i-1]
    valor_xb = rango_x[i]
    valor_xf = {"X":lmd*valor_xa + (1-lmd)*valor_xb}
    local_dict_xf = {**valor_xf}
    evaluacion = parse_expr(fun_original, local_dict_xf, transformations=transformaciones, evaluate=True)
    return evaluacion

def es_concava(fun_original,rango_lmd,rango_x):
    mensaje = f"la función: {fun_original} SI es Concava en el intervalo ({rango_x[0]:.2f}, {rango_x[-1]:.2f})."
    for lmd in rango_lmd:
        for i in range(1, len(rango_x)):
            valor_pivote = valor_funcion_pivote(fun_original,lmd,rango_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i)
            restriccion_concavidad = valor_fun_org_lmd <= valor_pivote
            if (not restriccion_concavidad):
                mensaje = f"la función: {fun_original} NO es Concava en el intervalo ({rango_x[0]:.2f}, {rango_x[-1]:.2f})."
                return mensaje
    return mensaje

def es_convexa(fun_original,rango_lmd,rango_x):
    mensaje = f"la función: {fun_original} SI es Convexa en el intervalo ({rango_x[0]:.2f}, {rango_x[-1]:.2f})."
    for lmd in rango_lmd:
        for i in range(1, len(rango_x)):
            valor_pivote = valor_funcion_pivote(fun_original,lmd,rango_x,i)
            valor_fun_org_lmd = valor_funcion_original_con_lambda(fun_original,lmd,rango_x,i)
            restriccion_concavidad = valor_fun_org_lmd >= valor_pivote
            if (not restriccion_concavidad):
                mensaje = f"la función: {fun_original} NO es Convexa en el intervalo ({rango_x[0]:.2f}, {rango_x[-1]:.2f})."
                return mensaje
    return mensaje

def evaluar_convexidad_y_concavidad(obj,fun_original,rango_lmd,rango_x):
    if obj == "convexa":
        return es_convexa(fun_original,rango_lmd,rango_x)
    elif obj == "concava":
        return es_concava(fun_original,rango_lmd,rango_x)
    else:
        mensaje = "Porfavor ingresar un objetivo valido: 'convexa' o 'concava'"
        return mensaje
    return

def main():
    # Objetivo de la evaluación
    obj = "concava"
    # Función a la que se le determinará si es concava o conexa
    fun_original = "ln(X)"
    # Valor de Lambda
    rango_lmd = linspace(0,1,20)
    # Rando de evaluación
    rango_x = linspace(0.1, 10, 100)
    # Resultado de la evalución
    resultado = evaluar_convexidad_y_concavidad(obj,fun_original,rango_lmd,rango_x)
    # Muestra el resultado en consola
    print(resultado)
    return

if __name__ == "__main__":
    main()