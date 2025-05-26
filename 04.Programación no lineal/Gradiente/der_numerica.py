
from numpy import pi
from sympy import sympify

def valor_fun_x(fun,x):
    evaluacion = sympify(fun).subs({"x":x})
    return evaluacion

def valor_fun_xh(fun,x,h):
    evaluacion = sympify(fun).subs({"x": x+h})
    return evaluacion

def derivada_numerica(fun,x,h):
    fun_x = valor_fun_x(fun,x)
    fun_xh = valor_fun_xh(fun,x,h)
    try:
        derivada = float(((fun_xh - fun_x) / h).evalf())
    except AttributeError:
        derivada = (fun_xh - fun_x) / h
    except TypeError:
        err = "err"
        mensaje = f"Derivada de la función {fun} NO esta definida en el punto: x={x}"
        return (mensaje, err)
        
    mensaje = f"La derivada de la función {fun} es: {derivada}."
    return (mensaje, derivada)

def main():
    # Función a la que se la buscará su derivada
    fun = "1/(x-2)"
    # Valor de X
    x = 2
    # Valor al que tiende delta x
    h = 1e-8
    # Resultado de la evaluación
    resultado = derivada_numerica(fun,x,h)
    # Muestra el resultado por consola
    print(resultado[0])
    return

if __name__ == "__main__":
    main()