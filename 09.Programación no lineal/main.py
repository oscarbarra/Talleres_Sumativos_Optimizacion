from sympy import sympify
from numpy import array, dot
from fun_aux.grad import encontrar_gradiente, evaluar_gradiente

def mostrar_valores_consola(message, vals, mod, n, tnew):
    cant_float = 32
    cant_hypen = 70
    print(f"{message[0]} : {float(vals[0]):.{cant_float}f}, {float(vals[1]):.{cant_float}f}")
    print(f"{message[1]} : {mod}")
    print(f"Valor eta : {n:.{cant_float}f}")
    print(f"Valor t   : {tnew}")
    print(f"{'-' * cant_hypen}")
    return

def modulo_no_sqrt(grad):
    return sum(value**2 for value in grad)

def barzilai_borwein(fun, vars, xnew, xold):
    subs_xnew = {vars[i]: xnew[i] for i in range(len(vars))}
    subs_xold = {vars[i]: xold[i] for i in range(len(vars))}

    grad_fun = encontrar_gradiente(fun, vars, 1)
    grad_new = evaluar_gradiente(grad_fun, subs_xnew)
    grad_old = evaluar_gradiente(grad_fun, subs_xold)

    delta_x = array(xnew) - array(xold)
    delta_grad = array(grad_new) - array(grad_old)

    num = dot(delta_x, delta_grad)
    den = modulo_no_sqrt(delta_grad)

    num = num if num >= 0 else -1 *num

    if den == 0:
        return 1e-16

    return num /den

def gradiente_descendiente(fun, vars, vals, eta):
    grad = encontrar_gradiente(fun, vars, 1)
    mod = modulo_no_sqrt(grad).subs({vars[i]: vals[i] for i in range(len(vars))})
    
    mostrar_valores_consola(["Valores iniciales", "Modulo inicial"], vals, mod, eta, None)

    xnew = array(vals, dtype=float)
    xold = array(vals, dtype=float)

    while mod >= eta:
        subs_dict = {vars[i]: xnew[i] for i in range(len(vars))}
        grad_eval = evaluar_gradiente(grad, subs_dict)
        mod = modulo_no_sqrt(grad_eval)

        tglex = -1 * array(grad_eval)
        tnew = barzilai_borwein(fun, vars, xnew, xold)

        xold = xnew.copy()
        xnew = xold + tnew * tglex

        mostrar_valores_consola(["Valores nuevos", "Modulo nuevo"], xnew, mod, eta, tnew)

    mostrar_valores_consola(["Valores final", "Modulo final"], xnew, mod, eta, tnew)
    return

def main():
    funciones = [ 
        "x**2 + y**2",
        "(x + 2*y - 7)**2 + (2*x + y - 5)**2",
        "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
    ]
    variables = ("x", "y")
    valores_iniciales = [0, 1]
    eta = 1e-8

    gradiente_descendiente(funciones[0], variables, valores_iniciales, eta)

if __name__ == "__main__":
    main()