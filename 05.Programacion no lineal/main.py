
from sympy import Matrix, diff, sympify

def part_1(func, vars, vals):
    subs_dict = {vars[i]: vals[i] for i in range(len(vars))}
    return sympify(func).subs(subs_dict)

def part_2(func, vars, vals, tgle):
    grad = Matrix([diff(func, v) for v in vars])
    subs_dict = {vars[i]: vals[i] for i in range(len(vars))}
    grad_eval = grad.subs(subs_dict)
    dx = Matrix(tgle)
    return (grad_eval.T * dx)[0]

def part_3(func, vars, vals, tgle, t):
    subs_dict = {vars[i]: vals[i] + t * tgle[i] for i in range(len(vars))}
    H = Matrix([[diff(func, v1, v2) for v2 in vars] for v1 in vars]).subs(subs_dict)
    dx = Matrix(tgle)
    return 0.5 * (dx.T * H * dx)[0]

def taylor(func, vars, vals, tgle, t):
    prt1 = part_1(func, vars, vals)
    prt2 = part_2(func, vars, vals, tgle)
    prt3 = part_3(func, vars, vals, tgle, t)
    
    print("Parte 1 (f(x)): ", prt1)
    print("Parte 2 (gradiente · Δx): ", prt2)
    print("Parte 3 (0.5 * Δxᵗ·H·Δx): ", prt3)

    return prt1 + prt2 + prt3

def main():
    func = "1.20*x + 1.16*y - 0.5*(2*x**2 + y**2 + (x + y)**2)"
    vars = ["x", "y"]
    vals = [0.23, 0.41]
    tgle = [0.01, 0.01]
    t = 0.01

    resultado = taylor(func, vars, vals, tgle, t)
    print("\nResultado de f(x + Δx) ≈", resultado)
    vals2 = [0.24,0.42]
    print("Resultado directo f(x + Δx) =", part_1(func,vars,vals2))

if __name__ == "__main__":
    main()