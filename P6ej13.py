# Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos, con while. 
# Reflexiona y escribe en el propio programa en forma de comentario, qué opción es mejor y por qué.
numero=int(input("Introduce un numero: "))
inicio=1
divisor=0
while inicio<=numero and divisor <3:
    #al tenerl la posibilidad de poder poner una condicion en el bucle, no necesito recorrer necesariamente todos los elementos
    #hasta llegar al numero , solo evaluar si tiene mas de 2 divisores.
    if numero%inicio==0:
        print(inicio)
        divisor+=1
    inicio+=1
if divisor!=2:
    print("El numero no es primo")
elif divisor==2:
    print("El numero es primo")


    