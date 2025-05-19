
from numpy import pi
from sympy import symbols, limit, sin, cos, tan, cot, sec, csc, sqrt, log, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
      convert_xor, implicit_multiplication_application

transformaciones = standard_transformations + (convert_xor,implicit_multiplication_application)
fun_especiales = {"sin":sin,"cos":cos,"tan":tan,"cot":cot,"sec":sec,"csc":csc,\
                  "sqrt":sqrt,"log":log,"ln":log,"e":E,"pi":pi}
h = symbols("h")

def valor_fun_original(fun_original,valor_x):
    local_dict = {"x":valor_x, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def valor_fun_modificada(fun_original,valor_x,h):
    variables  = {"x":valor_x + h}
    local_dict = {**variables, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def derivada_numerica(fun_original,valor_x,delta_x):
    fun_x = valor_fun_original(fun_original,valor_x)
    fun_xh = valor_fun_modificada(fun_original,valor_x,h)
    cociente = (fun_xh - fun_x) / h
    derivada = limit(cociente, h, delta_x)
    mensaje = f"La derivada de la función {fun_original} es: {derivada}."
    return mensaje

def main():
    # Función a la que se la buscará su derivada
    fun_original = "e^(x^2)"
    # Valor de X
    valor_x = 10
    # Valor al que tiende delta x
    delta_x = 0.0
    # Resultado de la evaluación
    resultado = derivada_numerica(fun_original,valor_x,delta_x)
    # Muestra el resultado por consola
    print(resultado)
    return

if __name__ == "__main__":
    main()