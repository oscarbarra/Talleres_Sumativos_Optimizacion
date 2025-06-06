
from numpy import array
from sympy import sympify,diff,Matrix


def part_1(func,vars,vals):
    subs_dict = {vars[i]:vals[i] for i in range(len(vars))}
    return sympify(func).subs(subs_dict)

def part_2(func,vars,vals,tgle):
    subs_dict = {vars[i]: vals[i] for i in range(len(vars))}
    dr1x = diff(func, vars[0], 1).subs(subs_dict)
    dr1y = diff(func, vars[1], 1).subs(subs_dict)
    grad = Matrix([dr1x, dr1y])
    dx = Matrix(tgle)
    return grad.T * dx

def part_3(func,vars,vals,tgle,t):
    def hessiana(func,vars,vals,tgle,t):
        subs_dict = {vars[i]:vals[i]+t*tgle[i] for i in range(len(vars))}
        dr2x  = diff(func,vars[0],2).subs(subs_dict)
        dr2y  = diff(func,vars[1],2).subs(subs_dict)
        dr1x  = diff(func,vars[0],1).subs(subs_dict)
        dr2xy = diff(dr1x,vars[1],1).subs(subs_dict)
        return array([[dr2x,dr2xy],[dr2xy,dr2y]])
    h  = hessiana(func,vars,vals,tgle,t)
    dx = Matrix(tgle)
    return 0.5 * (dx.T * h * dx)[0]

def taylor(func,vars,vals,tgle,t):
    prt1 = part_1(func,vars,vals)      # Escalar
    prt2 = part_2(func,vars,vals,tgle) # Escalar
    prt3 = part_3(func,vars,vals,tgle,t)
    print("parte 1: ",prt1)
    print("parte 2: ",prt2)
    print("parte 3: ",prt3)
    return

def main():
    func = "1.20*x + 1.16*y - 0.5*(2*x**2 + y**2 + (x + y)**2)"
    vars = ["x","y"]
    vals = [0.23,0.41]
    tgle = [0.01,0.01]
    t    =  0.01

    print("Teorema de Taylor: ",taylor(func,vars,vals,tgle,t))
    return

if __name__ == "__main__":
    main()