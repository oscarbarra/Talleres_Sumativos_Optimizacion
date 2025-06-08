
from numpy import array
from random import randint
from sympy import sqrt,sympify
from fun_aux.grad import encontrar_gradiente,evaluar_gradiente

def mostrar_valores_consola(message,vals,mod,n):
    cant_float = 32
    cant_hypen = 70
    print(message[0],f": {vals[0]:.{cant_float}f}, {vals[1]:.{cant_float}f}")
    print(message[1],f": {mod}")
    print("Valor eta: ",n)
    print(f"{'-':-<{cant_hypen}}")
    return

def modulo(grad):
    mod = 0
    for value in grad:
        mod += (value**2)
    return sympify(sqrt(mod))

def gradiente_descendiente(fun,vars,vals,t,n):
    grad = encontrar_gradiente(fun,vars,1)
    mod = modulo(grad).subs({vars[i]:vals[i] for i in range(len(vars))})
    vals_new = vals
    mostrar_valores_consola(["Valores iniciales","Modulo inicial"],vals_new,mod,n)
    while (mod >= n):
        tglex = -1 * array(evaluar_gradiente(grad,{vars[i]:vals_new[i] for i in range(len(vars))}))
        vals_old = vals_new
        vals_new = array(vals_old) + t*array(tglex)
        mod = modulo(grad).subs({vars[i]:vals_new[i] for i in range(len(vars))})
        mostrar_valores_consola(["Valores nuevos","Modulo nueva"],vals_new,mod,n)
    mostrar_valores_consola(["Valores final","Modulo final"],vals_new,mod,n)
    return

def main():
    fun = [ 
            "x**2 + y**2",
            "(x + 2*y - 7)**2 + (2*x + y - 5)**2",
            "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
        ]
    vars = ("x","y")
    vals = [randint(0,10),randint(0,10)]
    t = 0.1
    n = 1e-16
    gradiente_descendiente(fun[0],vars,vals,t,n)
    return

if __name__ == "__main__":
    main()