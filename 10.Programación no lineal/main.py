
from numpy import array,dot
from sympy import sympify,symbols,diff,hessian,sqrt

def get_gradient(func:str,vars:list):
    func = sympify(func)
    sym_vals = [symbols(var) for var in vars]
    return [diff(func,var) for var in sym_vals]

def get_hessian(func:str,vars:list):
    func = sympify(func)
    sym_vals = [symbols(var) for var in vars]
    return hessian(func, sym_vals)

def get_module(vector:list):
    return sqrt(sum(val**2 for val in vector))

def get_Xnew(Xold:list,evl_gradient_old:list,evl_hessian_old:list[list],t:float):
    inv_hessian  = evl_hessian_old.inv()                                     # Matriz
    Xnew = array(Xold) -t * dot(array(inv_hessian), array(evl_gradient_old)) # Vector
    return Xnew

def condition(Xold,Xnew):
    Xold = array(Xold)
    Xnew = array(Xnew)
    return get_module(Xnew - Xold)

def newton_method(func:str,eta:float,t:float,xval:list,xsim:list):
    vct_gradient = get_gradient(func, xsim)# Valor simbolico
    mtx_hessian  = get_hessian(func, xsim) # Valor simbolico

    Xold = [0,0]
    Xnew = xval.copy()
    while (condition(Xold,Xnew) >= eta):
        vals_dict_old = {xsim[i]:Xnew[i] for i in range(len(xsim))}
        evl_gradient_old = [grad.subs(vals_dict_old) for grad in vct_gradient] # old
        evl_hessian_old  = mtx_hessian.subs(vals_dict_old)

        Xold = Xnew.copy()
        Xnew = get_Xnew(Xold, evl_gradient_old, evl_hessian_old, t)
        
        vals_dict_new = {xsim[i]:Xnew[i] for i in range(len(xsim))}
        evl_gradient_new = [grad.subs(vals_dict_new) for grad in vct_gradient] # new

        if (get_module(evl_gradient_new) < get_module(evl_gradient_old)):
            aux1 = array(evl_gradient_new) - array(evl_gradient_old)
            
            g_cero = get_module(evl_gradient_old)           # Escalar
            g_cero_prima = -1 * (g_cero /get_module(aux1))  # Escalar
            g_uno = get_module(evl_gradient_new)            # Escalar

            aux2 = -1 *(g_cero/ (2*(g_uno - g_cero - g_cero_prima)))

            t_prima = max(aux2, 0.1)
            Xnew = (1 - t_prima) * array(Xold) + t_prima * array(Xnew)
        print("Xnew yo: ",Xnew)
    return

def main():
    func = [ 
            "x**2 + y**2",
            "(x + 2*y - 7)**2 + (2*x + y - 5)**2",
            "(x**2 + y - 11)**2 + (x + y**2 - 7)**2"
        ]
    eta  = 1e-6
    t    = 0.01
    xval = [-3,-3]
    xsim = ('x','y')
    newton_method(func[2],eta,t,xval,xsim)
    return

if __name__ == "__main__":
    main()