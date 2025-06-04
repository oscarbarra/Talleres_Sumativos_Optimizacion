
from numpy import array
from sympy import sqrt,sympify
from fun_aux.grad import encontrar_gradiente,evaluar_gradiente

def modulo(grad):
    mod = 0
    for value in grad:
        mod += (value**2)
    return sympify(sqrt(mod))

def gradiente_descendiente(fun,vars,vals,t,n):
    grad = encontrar_gradiente(fun,vars,1)
    mod = modulo(grad).subs({vars[i]:vals[i] for i in range(len(vars))})
    vals_new = vals
    while (mod >= n):
        tglex = -1 * array(evaluar_gradiente(grad,{vars[i]:vals_new[i] for i in range(len(vars))}))
        vals_old = vals_new
        vals_new = array(vals_old) + t*array(tglex)
        mod = modulo(grad).subs({vars[i]:vals_new[i] for i in range(len(vars))})
        print("Valores nuevo",f"{vals_new[0]:.16f}, {vals_new[1]:.16f}")
        print("Modulo nuevo: ", mod)
        print(f"{'-':-<55}")
    return

def main():
    fun = [ 
            "x**2 + y**2",
            "(x + 2*y -7)**2 + (2*x + y -5)**2",
            "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
        ]
    vars = ("x","y")
    vals = [2,2]
    t = 0.1
    n = 1e-16
    gradiente_descendiente(fun[1],vars,vals,t,n)
    return

if __name__ == "__main__":
    main()