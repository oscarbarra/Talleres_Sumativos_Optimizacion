
from numpy import pi
from sympy import sympify, symbols, limit

x,h = symbols("x h")

def valor_fun_x(fun):
    evaluacion = sympify(fun).subs({"x":x})
    return evaluacion

def valor_fun_xh(fun):
    evaluacion = sympify(fun).subs({"x":x+h})
    return evaluacion

def derivada_explicita(fun,valor_x):
    fun_x = valor_fun_x(fun)
    fun_xh = valor_fun_xh(fun)

    cociente = (fun_xh - fun_x) / h
    derivada = limit(cociente,h,0)
    eval_der = derivada.subs(x,valor_x).evalf()

    errores = ["oo", "-oo", "nan"]
    if str(eval_der) in errores:
        err = "err"
        mensaje = f"Derivada de la función {fun} NO esta definida en el punto: x={valor_x}"
        return (mensaje, err)

    mensaje = f"La derivada de la función {fun} es: {eval_der}."
    return (mensaje, eval_der)

def main():
    # Función a la que se la buscará su derivada
    fun = "1/(x-2)"
    # Valor de X
    valor_x = 0
    # Resultado de la evaluación
    der_imp = derivada_explicita(fun,valor_x)
    # Muestra el resultado por consola
    print(der_imp[0])
    return

if __name__ == "__main__":
    main()