
from der_numerica import derivada_numerica
from der_explicita import derivada_explicita
from gradiente import encontrar_gradiente, evaluar_gradiente, mostrar_resultados_en_consola

def calcular_derivada(tipo_der,fun,variables):
    der_validas = ("numerica", "explicita", "gradiente")
    if tipo_der not in der_validas:
        return print(f"Tipo de derivada NO soportado, Porfavor elegir entre {der_validas}")
    
    if tipo_der == "numerica":
        x = variables["x"]
        h = variables["h"]
        resultado = derivada_numerica(fun,x,h)
        return print(resultado[0])
    elif tipo_der == "explicita":
        x = variables["x"]
        resultado = derivada_explicita(fun,x)
        print(resultado[0])
    else:
        variables.pop("h", None) 
        gradiente = encontrar_gradiente(fun,variables)
        gradiente_evaluado = evaluar_gradiente(gradiente,variables)
        mostrar_resultados_en_consola(fun,gradiente,gradiente_evaluado,variables)
    return

def main():
    # 1.numerica, 2.explicita, 3.gradiente
    tipo_der = "gradiente"
    fun = "x**2 + y**3"
    variables = {"x":2,"y":3,"h":1e-6}
    calcular_derivada(tipo_der,fun,variables)
    return

if __name__ == "__main__":
    main()