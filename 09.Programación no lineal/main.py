
from numpy import array, dot
from fun_aux.grad import encontrar_gradiente, evaluar_gradiente

def modulo_no_sqrt(grad):
    return sum(value**2 for value in grad)

def barzilai_borwein(fun, vars, xnew, xold):
    subs_xnew = {vars[i]: xnew[i] for i in range(len(vars))}
    subs_xold = {vars[i]: xold[i] for i in range(len(vars))}

    grad_fun = encontrar_gradiente(fun, vars, 1)
    grad_new = evaluar_gradiente(grad_fun, subs_xnew)
    grad_old = evaluar_gradiente(grad_fun, subs_xold)

    aux1 = array(xold) - array(xnew)
    aux2 = array(grad_old) - array(grad_new)

    num = dot(aux1, aux2)
    den = modulo_no_sqrt(aux2)

    num = num if num >= 0 else -1 *num

    if den == 0:
        return 1e-16

    return num /den

def gradiente_descendiente(fun, vars, vals, eta):
    grad = encontrar_gradiente(fun, vars, 1)
    mod = modulo_no_sqrt(grad).subs({vars[i]: vals[i] for i in range(len(vars))})
    
    xnew = array(vals)
    xold = array(vals)

    while mod >= eta:
        subs_dict = {vars[i]: xnew[i] for i in range(len(vars))}
        grad_eval = evaluar_gradiente(grad, subs_dict)
        mod = modulo_no_sqrt(grad_eval)

        tglex = -1 * array(grad_eval)
        tnew = barzilai_borwein(fun, vars, xnew, xold)

        xold = xnew.copy()
        xnew = xold + tnew * tglex

        print("t: ",tnew)
        print("Xnew: ",xnew)
        print('-' * 55)
    return

def main():
    funciones = [ 
        "x**2 + y**2",
        "(x + 2*y - 7)**2 + (2*x + y - 5)**2",
        "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
    ]
    variables = ("x", "y")
    valores_iniciales = [-1,-5]
    eta = 1e-6

    gradiente_descendiente(funciones[2], variables, valores_iniciales, eta)

if __name__ == "__main__":
    main()