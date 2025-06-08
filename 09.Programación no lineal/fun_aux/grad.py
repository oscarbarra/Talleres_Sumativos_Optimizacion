

from sympy import symbols, sympify, diff

def mostrar_resultados_en_consola(fun, grad, grad_eval,vars):
    # valores = ", ".join(["{}={}".format(k, v) for k, v in vars.items()])
    print(f"El gradiente de la función: {fun}, es:")
    print(grad)
    print(f"El gradiente para los puntos {vars} es:")
    print(grad_eval)
    return

def deribada_parcial(fun_simb,var,orden):
    return diff(fun_simb,var,orden)

def evaluar_gradiente(gradiente,variables):
    gradiente_evaluado = list()
    for df_var in gradiente:
        # Evalua las derivadas parciales en los puntos dados
        df_eval = df_var.subs(variables)
        # Guarda el valor de la evaluación dentro de 'gradiente_evaluado'
        gradiente_evaluado.append(df_eval)
    return gradiente_evaluado

def encontrar_gradiente(fun,vars,orden=1):
    vars_simb = [symbols(var) for var in vars] 
    fun_simb = sympify(fun,convert_xor=True)
    grad = list()
    for var in vars_simb:
        # Calcula la derivada parcial de la función
        df_var = deribada_parcial(fun_simb,var,orden)
        # Guarda el valor de la derivada dentro del 'gradiente'
        grad.append(df_var)
    return grad

def main():
    fun = "x**3+ 6*y + 9"
    vars = ('x', 'y')
    grad = encontrar_gradiente(fun,vars,orden=2)
    print(evaluar_gradiente(grad,{'x':2,'y':3}))
    mostrar_resultados_en_consola(fun,grad,None,vars)
    return

if __name__ == "__main__":
    main()