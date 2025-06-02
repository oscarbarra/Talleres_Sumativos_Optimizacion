
from sympy import sympify, latex
from numpy import linspace,array
from matplotlib import pyplot as plt

from fun_auxiliares.gradiente import encontrar_gradiente

def graficar_resltados(fun,vals_x,vals_y,taylor):
    plt.title(f"Teorema de Tayler sobre la función ${latex(sympify(fun))}$")
    plt.plot(vals_x,vals_y,color='r',label="Exacta")
    plt.plot(vals_x,taylor,color='b',label="Taylor")
    plt.grid(True)
    plt.legend()
    plt.show()
    return

def teorema_taylor(fun,var,value,tgle_x,t):
    pgrad = array(encontrar_gradiente(fun,var,orden=1))
    sgrad = array(encontrar_gradiente(fun,var,orden=2))

    prt_2 = pgrad * tgle_x    
    prt_3 = 0.5 * tgle_x * sgrad * tgle_x

    prt_2_str = str(prt_2[0])
    prt_3_str = str(prt_3[0])

    taylor_1 = sympify(fun).subs({var:value})
    taylor_2 = sympify(prt_2_str).subs({var:value})
    taylor_3 = sympify(prt_3_str).subs({var:value + t*tgle_x})

    return taylor_1 + taylor_2 + taylor_3

def main():
    t = 1
    tgle_x = 0.01
    fun  = "x**2 - cos(x)"
    vals_x = linspace(0,1,100)
    var  = 'x'

    vals_y = [sympify(fun).subs({var:x}) for x in vals_x]
    taylor = [teorema_taylor(fun,var,value,tgle_x,t) for value in vals_x]

    graficar_resltados(fun,vals_x,vals_y,taylor)
    return

if __name__ == "__main__":
    main()