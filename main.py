### aquí se estarán implementando y mostrando los resultados de cada uno de los 
##algoritmos implementados.
import algoritmo1 as lol1
import algoritmo2 as lol2
import algoritmo3 as lol3
import time
import matplotlib.pyplot as plt


## este límite es para que no se tarde demasiado en ejecutar los algoritmos, ya que algunos de ellos 
# tienen una complejidad muy alta y podrían tardar demasiado tiempo en ejecutarse. El límite solo es de operaciones
limite = 5e7

algoritmos = [
    ("Algoritmo 1", lol1.algoritmo1, lol1.formula1),
    ("Algoritmo 2", lol2.algoritmo2, lol2.formula2),
    ("Algoritmo 3", lol3.algoritmo3, lol3.formula3),
]
## Función para medir el tiempo de ejecución de un algoritmo
def medir(func, n, repeticiones=3):
    """Mejor tiempo de varias corridas, en segundos."""
    mejor = float("inf")
    ## el _ es una convención para indicar que no se usará la variable de iteración
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        func(n)
        mejor = min(mejor, time.perf_counter() - t0)
    return mejor

# Al ser una gran cantidad de código, preferí hacer una función main para facilitar la lectura 
# luego solo se estará ejecutando dentro del verdadero main. 
def main():
    ns = [1, 10, 100, 1000, 10000, 100000, 1000000]
    ## en esta sección se estarán ejecutando los algoritmos y mostrando los resultados de cada uno de ellos
    ## diccionario para almacenar los resultados de cada algoritmo
    resultados = {}
    for nombre, func, formula in algoritmos:
        filas = []
        ultima_razon = None   # segundos por operación
        print(f"\n{nombre}")
        print(f"{'n':>9} | {'operaciones':>16} | {'tiempo (s)':>14} | nota")
        print("-" * 60)
        ## se itera sobre los valores de n para cada algoritmo
        for n in ns:
            ops = formula(n)
            if ops <= limite:
                reps = 3 if ops < 1e6 else 1
                t = medir(func, n, reps)
                assert func(n) == ops, "la fórmula no coincide con el conteo real"
                if ops > 0:
                    ultima_razon = t / ops
                estimado = False
            else:
                t = ops * ultima_razon
                estimado = True
            filas.append((n, ops, t, estimado))
            nota = "estimado" if estimado else ""
            print(f"{n:>9} | {ops:>16,} | {t:>14.6g} | {nota}")
        resultados[nombre] = filas
        
    ## sección para realizar las gráficas de los resultados 
    ## se crean tres subplots, uno para cada algoritmo, con un tamaño de figura de 17x4.5 pulgadas
    fig, ejes = plt.subplots(1, 3, figsize=(17, 4.5))
    ## se itera sobre los ejes y los resultados de cada algoritmo para graficar los tiempos y las operaciones
    for ax, (nombre, filas) in zip(ejes, resultados.items()):
        ## se separan los valores de n, operaciones y tiempos en listas para graficar
        ns = [f[0] for f in filas]
        ops = [f[1] if f[1] > 0 else float("nan") for f in filas]   # 0 no cabe en escala log
        ts = [f[2] for f in filas]
        ## se grafican los tiempos en azul y las operaciones en rojo, con escalas logarítmicas en ambos ejes
        ax.plot(ns, ts, "o-", color="tab:blue", label="Tiempo (s)")
        ## se grafican los puntos estimados con un marcador de círculo blanco y borde azul
        est = [(f[0], f[2]) for f in filas if f[3]]
        ## si hay puntos estimados, se grafican con un marcador de círculo blanco y borde azul
        if est:
            ax.plot(*zip(*est), "o", mfc="white", color="tab:blue", label="Tiempo estimado")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("n")
        ax.set_ylabel("Tiempo (s)", color="tab:blue")
        # se crea un segundo eje y para graficar las operaciones en rojo
        ax2 = ax.twinx()
        ax2.plot(ns, ops, "s--", color="tab:red", label="Operaciones")
        ax2.set_yscale("log")
        ax2.set_ylabel("Operaciones", color="tab:red")
        # se establece el título del subplot con el nombre del algoritmo y se combinan las leyendas de ambos ejes
        ax.set_title(nombre)
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)
    # se ajusta el diseño de la figura para que no se solapen los elementos y se guarda la figura en un archivo PNG con una resolución de 150 dpi
    plt.tight_layout()
    plt.savefig("resultados_lab.png", dpi=150)
    plt.show()
    
if __name__ == "__main__":
    main()
    