
from numpy import pi
from sympy import symbols, limit, sin, cos, tan, cot, sec, csc, sqrt, log, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, \
      convert_xor, implicit_multiplication_application

transformaciones = standard_transformations + (convert_xor,implicit_multiplication_application)
fun_especiales = {"sin":sin,"cos":cos,"tan":tan,"cot":cot,"sec":sec,"csc":csc,\
                  "sqrt":sqrt,"log":log,"ln":log,"e":E,"pi":pi}

x,h = symbols("x h")

def valor_fun_x(fun_original):
    local_dict = {"x":x, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def valor_fun_xh(fun_original):
    variables  = {"x":x + h}
    local_dict = {**variables, **fun_especiales}
    evaluacion = parse_expr(fun_original, local_dict=local_dict, transformations=transformaciones, evaluate=True)
    return evaluacion

def derivada_explicita(fun_original,valor_x):
    fun_x = valor_fun_x(fun_original)
    fun_xh = valor_fun_xh(fun_original)

    cociente = (fun_xh - fun_x) / h
    derivada = limit(cociente,h,0)
    eval_der = derivada.subs(x,valor_x).evalf()

    errores = ["oo", "-oo", "nan"]
    if str(eval_der) in errores:
        err = "err"
        mensaje = f"Derivada de la función {fun_original} NO esta definida en el punto: x={valor_x}"
        return (mensaje, err)

    mensaje = f"La derivada de la función {fun_original} es: {eval_der}."
    return (mensaje, eval_der)

def main():
    # Función a la que se la buscará su derivada
    fun_original = "1/(x-2)"
    # Valor de X
    valor_x = 0
    # Resultado de la evaluación
    der_imp = derivada_explicita(fun_original,valor_x)
    # Muestra el resultado por consola
    print(der_imp[0])
    return

if __name__ == "__main__":
    main()