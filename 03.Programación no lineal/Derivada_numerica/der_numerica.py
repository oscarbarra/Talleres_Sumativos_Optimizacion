
from numpy import isclose, pi
from sympy import sin, cos, tan, cot, sec, csc, sqrt, log, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
      convert_xor, implicit_multiplication_application

transformaciones = standard_transformations + (convert_xor,implicit_multiplication_application)
fun_especiales = {"sin":sin,"cos":cos,"tan":tan,"cot":cot,"sec":sec,"csc":csc,\
                  "sqrt":sqrt,"log":log,"ln":log,"e":E,"pi":pi}

def valor_fun_x(fun_original,x):
    local_dict = {"x":x, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def valor_fun_xh(fun_original,x,h):
    variables  = {"x":x + h}
    local_dict = {**variables, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def derivada_numerica(fun_original,x,h):
    fun_x = valor_fun_x(fun_original,x)
    fun_xh = valor_fun_xh(fun_original,x,h)
    try:
        derivada = float(((fun_xh - fun_x) / h).evalf())
    except AttributeError:
        derivada = (fun_xh - fun_x) / h
    except TypeError:
        err = "err"
        mensaje = f"Derivada de la función {fun_original} NO esta definida en el punto: x={x}"
        return (mensaje, err)
        
    mensaje = f"La derivada de la función {fun_original} es: {derivada}."
    return (mensaje, derivada)

def main():
    # Función a la que se la buscará su derivada
    fun_original = "1/(x-2)"
    # Valor de X
    x = 0
    # Valor al que tiende delta x
    h = 1e-8
    # Resultado de la evaluación
    resultado = derivada_numerica(fun_original,x,h)
    # Muestra el resultado por consola
    print(resultado[0])
    return

if __name__ == "__main__":
    main()