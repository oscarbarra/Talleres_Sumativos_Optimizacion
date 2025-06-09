
from numpy import array
from sympy import sympify,symbols,diff,hessian,sqrt

def get_gradient(func:str,vars:list):
    func = sympify(func)
    vars_sym = [symbols(var) for var in vars]
    return [diff(func,var) for var in vars_sym]

def get_hessian(func:str,vars:list):
    func = sympify(func)
    vars_sym = [symbols(var) for var in vars]
    return hessian(func, vars_sym)

def get_module(vector):
    return sqrt(sum(val**2 for val in vector))

def newton_method(func:str,eta:float,t:float,xval:list,xsim:list):
    gradient = get_gradient(func,xsim)      # Valor simbolico
    hessian  = get_hessian(func,xsim) # Valor simbolico

    Xnew = xval # Vector
    while (True): #get_module([2,2]) <= eta
        vals_dict = {xsim[i]:xval[i] for i in range(len(xsim))}
        gradient_eval = [grad.subs(vals_dict) for grad in gradient]
        hessian_eval  = hessian.subs(vals_dict)
        print(gradient_eval)
        print(hessian_eval)
        Xnew = array(Xnew) -t*array(hessian_eval)*array(gradient_eval)
        print(Xnew)
        break
    return

def main():
    func = "x**2 + y**3"
    eta  = 1e-8
    t    = 0.01
    xval = (1,1)
    xsim = ('x','y')
    newton_method(func,eta,t,xval,xsim)
    return

if __name__ == "__main__":
    main()