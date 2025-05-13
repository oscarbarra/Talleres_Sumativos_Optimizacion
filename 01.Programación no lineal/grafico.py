
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def interseccion_rectas(A1, b1, A2, b2):
    # Resuelve el sistema de ecuaciones lineales A1 * [x1, x2] = b1 y A2 * [x1, x2] = b2
    A = np.vstack([A1, A2])
    b = np.array([b1, b2])
    try:
        interseccion = np.linalg.solve(A, b)
        return interseccion
    except np.linalg.LinAlgError:
        # Si no tiene solución única, las rectas son paralelas
        return None

def encuentra_vertices_interseccion(A, b, signs):
    vertices = []
    # Recorremos todas las combinaciones de restricciones
    for i in range(A.shape[0]):
        for j in range(i + 1, A.shape[0]):
            # Si las restricciones son diferentes (y no paralelas), calculamos la intersección
            interseccion = interseccion_rectas(A[i], b[i], A[j], b[j])
            if interseccion is not None:
                # Verificamos si el punto está dentro de la región factible
                x1, x2 = interseccion
                if 0 <= x1 <= 5 and 0 <= x2 <= 5:  # Limitar el rango para la visualización
                    # Verificamos si cumple con las restricciones
                    cumple = True
                    for k in range(A.shape[0]):
                        if signs[k] == "<=" and not (A[k, 0] * x1 + A[k, 1] * x2 <= b[k]):
                            cumple = False
                        elif signs[k] == ">=" and not (A[k, 0] * x1 + A[k, 1] * x2 >= b[k]):
                            cumple = False
                    if cumple:
                        vertices.append([x1, x2])
    return np.array(vertices)

def graficar(A, b, signs, solucion, teta):
    # Encontramos los vértices de intersección entre las restricciones
    vertices = encuentra_vertices_interseccion(A, b, signs)
    
    # Dibujar las restricciones
    x1_vals = np.linspace(0, 5, 100)
    for i in range(len(A)):
        if A[i, 1] != 0:
            x2_vals = (b[i] - A[i, 0] * x1_vals) / A[i, 1]
            plt.plot(x1_vals, x2_vals, label=f'Restricción {i+1}')
        else:
            plt.axvline(x=b[i]/A[i, 0], label=f'Restricción {i+1}')
    
    # Crear el polígono que representa la región factible
    if len(vertices) > 2:
        poly = Polygon(vertices, color='lightblue', alpha=0.5, label='Región factible')
        plt.gca().add_patch(poly)

    # Dibujar los vértices de la región factible
    plt.scatter(vertices[:, 0], vertices[:, 1], color='blue', s=50)

    # Dibujar el punto óptimo
    plt.scatter(solucion[0][0], solucion[0][1], color='red', label='Punto óptimo', s=100, edgecolor='black')
    plt.annotate(f'({solucion[0][0]:.2f}, {solucion[0][1]:.2f}, {solucion[1]:.2f})', xy=(solucion[0][0], solucion[0][1]), xytext=(solucion[0][0]+0.1, solucion[0][1]+0.1))

    plt.legend(title=f'Teta: {teta}')

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Optimización con Fuerza Bruta')
    plt.grid(True)
    plt.ylim(-1, 6)
    plt.xlim(-1, 6)
    plt.show()
    return
