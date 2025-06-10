
from numpy import array
from fun_aux.grad import encontrar_gradiente,evaluar_gradiente

def modulo(grad):
    return (sum(val**2 for val in grad))

def gradiente_descendiente(fun,vars,vals,t,n):
    subs_dict_init = {vars[i]:vals[i] for i in range(len(vars))}
    grad = encontrar_gradiente(fun,vars,1)
    mod = modulo(grad).subs(subs_dict_init)

    vals_new = vals.copy()
    while (mod >= n):
        subs_dict_old = {vars[i]:vals_new[i] for i in range(len(vars))}
        tglex = -1 * array(evaluar_gradiente(grad,subs_dict_old))
        vals_new = array(vals_new) + t * array(tglex)

        subs_dict_new = {vars[i]:vals_new[i] for i in range(len(vars))}
        mod = modulo(grad).subs(subs_dict_new)
        
        print("vals new: ",vals_new)
    return

def main():
    fun = [ 
            "x**2 + y**2",
            "(x + 2*y - 7)**2 + (2*x + y - 5)**2",
            "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
        ]
    vars = ("x","y")
    vals = [-3,5]
    t = 0.1
    n = 1e-7
    gradiente_descendiente(fun[2],vars,vals,t,n)
    return

if __name__ == "__main__":
    main()