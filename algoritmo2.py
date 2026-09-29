### Segundo algoritmo del laboratorio
## algoritmo de ejemplo hecho en otro lenguaje de programación 
# if (n <= 1) return;
##int i,j;
##for (i = 1; i <= n; i++){
### for (j = 1; j <= n; j++){
### printf("Sequence\n");
### break;
### }
##}
#}

##ahora en python este sería el equivalente
def function2(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break