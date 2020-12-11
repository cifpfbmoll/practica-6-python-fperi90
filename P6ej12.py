# Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar). 
# El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata.
# El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.
# Valor mínimo: 0
# Valor máximo: 100
# Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
# Es 50 ?: mayor
# Es 75 ?: menor
# Es 62 ?: menor
# Es 56 ?: mayor
# Es 59 ?: igual
minimo=int(input("Valor minimo: "))
maximo=int(input("Valor maximo: "))
primero=maximo/2
print("Piensa un numero entre ",minimo,"y",maximo,"a ver si lo puedo adivinar")
print("Es ",primero,"?: ",end="")
palabra=str(input())
while palabra=="mayor":# tengo que admitir que lo que mas me ayudo en este ejericio ha sido hacer el pseudocodigo en una hoja aparte.
    #a partir de ahora todos los ejercicios seran asi
    minimo=primero
    primero=minimo+((maximo-minimo)/2)
    print("Es ",primero,"? ",end="")
    palabra=str(input())
    while palabra=="menor":
        maximo=primero
        primero=minimo+((maximo-minimo)/2)
        print("Es ",primero,"? ",end="")
        palabra=str(input())
while palabra=="menor":
    maximo=primero
    primero=minimo+((maximo-minimo)/2)
    print("Es ",primero,"? ",end="")
    palabra=str(input())
    while palabra=="mayor":
        minimo=primero
        primero=minimo+((maximo-minimo)/2)
        print("Es ",primero,"? ",end="")
        palabra=str(input())
if palabra=="igual":
    print("finalizado")