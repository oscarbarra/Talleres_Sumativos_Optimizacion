
import sys
from pathlib import Path

# Sube dos niveles: desde "Err en la Derivada" hasta "03.Programación no lineal"
ruta_padre = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta_padre))

from Derivada_numerica.der_numerica import derivada_numerica
from der_explicita import derivada_explicita

def valor_inicial_delta_x(epsilon,x,mar_err=1e-6):
    if x == 0:
        delta_x = (epsilon**0.5 * x) + mar_err
    else:
        delta_x = epsilon**0.5 * x
    return delta_x

def margen_error(der_exp,der_num,epsilon):
    error = abs(der_exp - der_num) < epsilon
    return error

def delta_x_optimo(fun_original,valor_x,epsilon):
    delta_x = valor_inicial_delta_x(epsilon,valor_x)
    der_exp = derivada_explicita(fun_original,valor_x)[1]
    der_num_inicial = derivada_numerica(fun_original,valor_x,delta_x)[1]

    err = "err"
    if der_exp == err or der_num_inicial == err:
        mensaje = f"Derivada de la función {fun_original} NO esta definida en el punto: x={valor_x}"
        return (mensaje, err)

    max_ciclos = 256
    condicion1 = max_ciclos > 0
    condicion2 = margen_error(der_exp,der_num_inicial,epsilon)
    while (condicion1 and not condicion2):
        max_ciclos -= 1
        delta_x   *= 10**(-1)
        der_num    = derivada_numerica(fun_original,valor_x,delta_x)[1]
        condicion2 = margen_error(der_exp,der_num,epsilon)
        condicion1 = max_ciclos > 0

    if (not condicion1):
        limite = "limite de ciclos alcanzados"
        mensaje = f"No se encontró un delta_x que cumpla con el margen de error, {limite}"
        return (mensaje, limite)
    
    mensaje = f"Para la derivada de la función: {fun_original}, en el punto: x={valor_x} \n" +\
              f"El valor sub optimo de delta_x es: {delta_x} \n" +\
              f"Valor derivada explicita: {der_exp} \n" +\
              f"Valor derivada numerica con el valor sub optimo de delta_x: {derivada_numerica(fun_original,valor_x,delta_x)[1]}"
    return (mensaje, delta_x)

def main():
    # Función a la que se la buscará su derivada
    fun_original = "1/(x-2)"
    # Valor de X
    valor_x = 0
    # Valor de epsilon
    epsilon = 1e-6
    # Resultado de la evalución
    resultado = delta_x_optimo(fun_original,valor_x,epsilon)
    # Muestra el resultado por consola
    print(resultado[0])
    return

if __name__ == "__main__":
    main()