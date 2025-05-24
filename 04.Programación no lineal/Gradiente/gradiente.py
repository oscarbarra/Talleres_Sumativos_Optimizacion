
from sympy import symbols, sympify, diff

def mostrar_resultados_en_consola(funcion, gradiente, gradiente_evaluado,variables):
    valores = ", ".join(["{}={}".format(k, v) for k, v in variables.items()])
    print(f"El gradiente de la función: {funcion}, es:")
    print(gradiente)
    print(f"El gradiente para los puntos {valores} es:")
    print(gradiente_evaluado)
    return

def deribada_parcial(funcion_simbolica,var):
    return diff(funcion_simbolica,var)

def encontrar_gradiente(funcion,variables): 
    funcion_simbolica = sympify(funcion)
    variables_simbolicas = [symbols(var) for var in variables.keys()]
    gradiente = list()
    for var in variables_simbolicas:
        # Calcula la derivada parcial de la función
        df_var = deribada_parcial(funcion_simbolica,var)
        # Guarda el valor de la derivada dentro del 'gradiente'
        gradiente.append(df_var)
    return gradiente

def evaluar_gradiente(gradiente,variables):
    gradiente_evaluado = list()
    for df_var in gradiente:
        # Evalua las derivadas parciales en los puntos dados
        df_eval = df_var.subs(variables)
        # Guarda el valor de la evaluación dentro de 'gradiente_evaluado'
        gradiente_evaluado.append(df_eval)
    return gradiente_evaluado

def main():
    funcion = "x^2 + x*y*p + y^2"
    variables = {"x":2, "y":3}
    gradiente = encontrar_gradiente(funcion,variables)
    gradiente_evaluado = evaluar_gradiente(gradiente,variables)
    mostrar_resultados_en_consola(funcion,gradiente,gradiente_evaluado,variables)
    return

if __name__ == "__main__":
    main()