
from numpy import isclose, pi
from sympy import sin, cos, tan, cot, sec, csc, sqrt, log, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
      convert_xor, implicit_multiplication_application

transformaciones = standard_transformations + (convert_xor,implicit_multiplication_application)
fun_especiales = {"sin":sin,"cos":cos,"tan":tan,"cot":cot,"sec":sec,"csc":csc,\
                  "sqrt":sqrt,"log":log,"ln":log,"e":E,"pi":pi}

def calcular_atol(valor1, valor2, epsilon=1e-8):
    max_val = max(abs(valor1), abs(valor2))
    return epsilon * max_val

def valor_fun_x(fun_original,valor_x):
    local_dict = {"x":valor_x, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def valor_fun_xh(fun_original,valor_x,h):
    variables  = {"x":valor_x + h}
    local_dict = {**variables, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def derivada_numerica(fun_original,valor_x,delta_x,margen_eval=1e-6):
    lado_der = delta_x + margen_eval
    lado_izq = delta_x - margen_eval

    derivada = [None, None]
    lados_eval = [lado_der, lado_izq]

    fun_x = valor_fun_x(fun_original,valor_x)
    for i in range(2):
        fun_xh = valor_fun_xh(fun_original,valor_x,lados_eval[i])
        try:
            derivada[i] = float(((fun_xh - fun_x) / lados_eval[i]).evalf())
        except AttributeError:
            derivada[i] = (fun_xh - fun_x) / lados_eval[i]
        except TypeError:
            fun_derivada = f"({fun_xh}-1*({fun_x}))/{lados_eval[i]}"
            mensaje = f"Posible asintota detectada, la función: {fun_derivada}" + \
                f" puede tener tendencia al infinito en el punto x = {valor_x}"
            return mensaje
        
    atol = calcular_atol(derivada[0],derivada[1],epsilon=1e-8)
    son_cercanos = isclose(derivada[0],derivada[1],rtol=1e-4,atol=atol)
    mensaje = f"La derivada de la función {fun_original} es: {derivada[0]}."
    if not (son_cercanos):
        mensaje = f"La función {fun_original} NO tiene una dervidad definida."
        return mensaje
    return mensaje

def main():
    # Función a la que se la buscará su derivada
    fun_original = "1/x"
    # Valor de X
    valor_x = 0.0
    # Valor al que tiende delta x
    delta_x = 0.0
    # Resultado de la evaluación
    resultado = derivada_numerica(fun_original,valor_x,delta_x)
    # Muestra el resultado por consola
    print(resultado)
    return

if __name__ == "__main__":
    main()