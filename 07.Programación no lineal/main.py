
from sympy import sympify,diff

def optimos_locales(func,vars,vals):
    func  = sympify(func)

    # Derivadas de primer orden
    dr1x  = diff(func,vars[0],1).subs({vars[i]:vals[i] for i in range(len(vars))}) # fx
    dr1y  = diff(func,vars[1],1).subs({vars[i]:vals[i] for i in range(len(vars))}) # fy

    if (dr1x != 0 or dr1y != 0):
        return f"El punto ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]}) no es un punto crítico (gradiente distinto de cero)"

    # Derivadas de segundo orden
    dr2x  = diff(func,vars[0],2).subs({vars[i]:vals[i] for i in range(len(vars))}) # fxx
    dr2y  = diff(func,vars[1],2).subs({vars[i]:vals[i] for i in range(len(vars))}) # fyy
    dr2xy = diff(dr1x,vars[1],1).subs({vars[i]:vals[i] for i in range(len(vars))}) # fxy

    # Determinante de la matriz hessiana
    h = dr2x * dr2y - dr2xy**2

    if (h == 0):
        return f"No existe información suficiente sobre el punto ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]})"
    elif (h < 0):
        return f"El punto ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]}) es un punto silla"
    elif (h > 0 and dr2x < 0):
        return f"El punto ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]}) es un maximo local"
    elif (h > 0 and dr2x > 0):
        return f"El punto ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]}) es un minimo local"
    return "A ocurrido un error inesperado"

def main():
    func = "x**2 + y**2"
    vars = ["x", "y"]
    vals = [0,1]
    
    print("Función: ",func)
    print(f"Punto de evaluación: ({vars[0]}:{vals[0]}, {vars[1]}:{vals[1]})")
    print(optimos_locales(func,vars,vals))
    return

if __name__ == "__main__":
    main()