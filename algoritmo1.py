### Primer algoritmo del laboratorio
## algoritmo de ejemplo hecho en otro lenguaje de programación 
# void function (int n ){
##int i,j,k, counter = 0;
##for (i = n/2; i <= n; i++){
### for (j = 1; j + n/2 <= n; j++){
#### for (k = 1; k <= n; k = k*2){
#### }
###}
##}
#}

##ahora en python este sería el equivalente 
def algoritmo1(n):
    counter = 0
    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1
            while k <= n:
                counter += 1
                k = k * 2
    return counter
