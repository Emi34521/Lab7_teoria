### aquí se estarán implementando y mostrando los resultados de cada uno de los 
##algoritmos implementados.
import algoritmo1 as lol1
import algoritmo2 as lol2
import algoritmo3 as lol3

if __name__ == "__main__":
    print ("A continuación se le estarán mostrando los resultadso de cada uno de los diferentes algoritmos del laboratorio 7 \n")
    print ("Primero que nada, seleccione el tipo de lagoritmo que desea ejecutar")
    md = int(input("1. Algori1tmo 1\n 2. Algoritmo 2\n 3. Algoritmo 3\n 0. Salir\n"))
    while (True):
        if (md == 1):
            real = lol1.algoritmo1(10)
            print("El resultado del algoritmo 1 es: ", real)
            md = 4
        elif (md == 2):
            lol2.function2(10)
            md = 4
        elif (md == 3):
            lol3.function3(10)
            md = 4
        elif (md == 0):
            print("Saliendo del programa.")
            break 
        elif (md == 4):
            md = int(input("1. Algori1tmo 1\n 2. Algoritmo 2\n 3. Algoritmo 3\n 4. Salir\n"))
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            md = int(input("1. Algoritmo 1\n 2. Algoritmo 2\n 3. Algoritmo 3\n"))
    print ("....")
    