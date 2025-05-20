
import sys
from pathlib import Path

# Sube dos niveles: desde "Err en la Derivada" hasta "03.Programación no lineal"
ruta_padre = Path(__file__).resolve().parent.parent
sys.path.append(str(ruta_padre))

from Derivada_numerica.der_numerica import derivada_numerica
from der_explicita import derivada_explicita

def valor_delta_x(epsilon,x):
    delta_x = epsilon**0.5 * x
    return delta_x

def margen_error(der_exp,der_num,epsilon):
    error = abs(der_exp -der_num) < epsilon
    return error

def main():
    # Función a la que se la buscará su derivada
    fun_original = "x^2"
    # Valor de X
    valor_x = 0.1
    # Valor de epsilon
    epsilon1 = 2.22e-16
    epsilon2 = 1.00e-8
    # Valor al que tiende delta x
    delta_x = valor_delta_x(epsilon2,valor_x)
    # Resultado exacto de la derivada
    der_exp = derivada_explicita(fun_original,valor_x)[1]
    # Resultado aproximado de la derivada
    der_num = derivada_numerica(fun_original,valor_x,delta_x)[1]
    # Resultado de la evalución
    resultado = margen_error(der_exp,der_num,epsilon2)
    print(resultado)
    return

if __name__ == "__main__":
    main()