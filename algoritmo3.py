#####0 Tercer algoritmo del laboratorio
## algoritmo de ejemplo hecho en otro lenguaje de programación 
# if (n <= 1) return;
##int i,j;
##for (i = 1; i <= n/3; i++){
### for (j = 1; j <= n; j+= 4){
### printf("Sequence\n");
### break;
### }
##}
#}

##ahora en python este sería el equivalente
def algoritmo3(n):
    if n <= 1:
        return 0
    counter = 0
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):  
            counter += 1
            break
    return counter
## función auxiliar para calcular la cantidad de operaciones que realiza el algoritmo 3
def formula3(n):
    return 0 if n <= 1 else n // 3