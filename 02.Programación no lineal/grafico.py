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
    plt.figure(figsize=(10, 5))
    plt.plot(x_pivote, y_real, label="f(x)", color="blue")
    plt.plot(x_pivote, y_pivote, label="Recta pivote", color="red", linestyle="--")

    # Márgenes dinámicos
    y_total = y_real + y_pivote + [fxa, fxb]
    y_min, y_max = min(y_total), max(y_total)
    margen = (y_max - y_min) * 0.1
    y_lim_inf = y_min - margen
    y_lim_sup = y_max + margen

    plt.axvline(valores_x[0], color="k", linestyle="--", label="Intervalo de x")
    plt.axvline(valores_x[-1], color="k", linestyle="--")

    plt.annotate(f"({x_pivote[0]:.2f}, {y_real[0]:.2f})",
                 xy=(x_pivote[0], y_real[0]),
                 xytext=(x_pivote[0]+0.1, y_real[0]+0.1),
                 arrowprops=dict(arrowstyle="->"))

    plt.annotate(f"({x_pivote[-1]:.2f}, {y_real[-1]:.2f})",
                 xy=(x_pivote[-1], y_real[-1]),
                 xytext=(x_pivote[-1]-0.1, y_real[-1]+0.15),
                 arrowprops=dict(arrowstyle="->"))

    plt.ylim(y_lim_inf, y_lim_sup)
    plt.title(resultado)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    fun = "sin(x)"
    valores_x = linspace(0, pi, 100)
    valores_lmd = linspace(0,1,20)
    crea_grafico(fun, valores_x, valores_lmd,"grafico de pruebas")

if __name__ == "__main__":
    main()