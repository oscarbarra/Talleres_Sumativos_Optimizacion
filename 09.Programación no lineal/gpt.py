
import numpy as np
import sympy as sp

# Paso 1: Gradiente simbólico
def calcular_gradiente(fun, vars):
    return [sp.diff(fun, v) for v in vars]

# Paso 2: Evaluar gradiente
def evaluar_gradiente(grad, vals_dict):
    return np.array([g.evalf(subs=vals_dict) for g in grad], dtype=float)

# Paso 3: Norma sin raíz cuadrada (para estabilidad)
def modulo_no_sqrt(vec):
    return float(np.dot(vec, vec))

# Paso 4: Barzilai-Borwein (cálculo de t)
def barzilai_borwein(x_new, x_old, grad_new, grad_old):
    s = x_new - x_old
    y = grad_new - grad_old

    num = np.dot(s, y)
    den = np.dot(y, y)

    if den == 0:
        return 1e-8  # paso mínimo para evitar división por 0

    return abs(num / den)  # usamos valor absoluto para evitar signo negativo

# Paso 5: Gradiente descendiente con BB
def gradiente_descendiente_bb(fun_expr, var_names, x0, eta=1e-8, max_iter=1000):
    vars = sp.symbols(var_names)
    fun = sp.sympify(fun_expr)
    grad = calcular_gradiente(fun, vars)

    x_new = np.array(x0, dtype=float)
    x_old = x_new - np.ones_like(x_new) * 0.1  # pequeña diferencia inicial

    for i in range(max_iter):
        vals_dict = {vars[j]: x_new[j] for j in range(len(vars))}
        grad_new = evaluar_gradiente(grad, vals_dict)

        mod_grad = modulo_no_sqrt(grad_new)
        if mod_grad < eta:
            break

        vals_dict_old = {vars[j]: x_old[j] for j in range(len(vars))}
        grad_old = evaluar_gradiente(grad, vals_dict_old)

        t = barzilai_borwein(x_new, x_old, grad_new, grad_old)

        x_next = x_new - t * grad_new
        x_old = x_new
        x_new = x_next

        print(f"Iteración {i+1}: x = {x_new}, t = {t}, ||grad||² = {mod_grad}")

    return x_new

# Ejemplo de uso
if __name__ == "__main__":
    resultado = gradiente_descendiente_bb("(x + 2*y - 7)**2 + (2*x + y - 5)**2", "x y", [0, 0])
    print("\nMínimo encontrado en:", resultado)