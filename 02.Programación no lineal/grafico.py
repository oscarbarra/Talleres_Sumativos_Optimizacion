from sympy import sympify
from numpy import linspace,pi
import matplotlib.pyplot as plt

def crea_grafico(fun, valores_x,valores_lmd,resultado):
    f = sympify(fun)
    x_a = valores_x[0]
    x_b = valores_x[-1]

    # Recta pivote: combinación convexa de f(x_a) y f(x_b)
    fxa = float(f.subs({"x": x_a}))
    fxb = float(f.subs({"x": x_b}))
    x_pivote = []
    y_pivote = []
    y_real = []

    for lmd in valores_lmd:
        x = lmd * x_a + (1 - lmd) * x_b
        y_p = lmd * fxa + (1 - lmd) * fxb
        y_f = float(f.subs({"x": x}))
        x_pivote.append(x)
        y_pivote.append(y_p)
        y_real.append(y_f)

    # Gráfico
    plt.plot(x_pivote, y_real, label="f(x)", color="blue")
    plt.plot(x_pivote, y_pivote, label="Recta pivote", color="red", linestyle="--")
    plt.title(resultado)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    fun = "sin(x)"
    valores_x = linspace(0, pi, 100)
    valores_lmd = linspace(0,1,20)
    crea_grafico(fun, valores_x, valores_lmd)

if __name__ == "__main__":
    main()