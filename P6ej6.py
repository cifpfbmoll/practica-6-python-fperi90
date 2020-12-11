# Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.
# Escribe un número: 6
# Escribe un número mayor que 6: 4
# 4 no es mayor que 6. Vuelve a probar: 50
# Escribe un número entre 6 y 50: 45
# Escribe otro número entre 6 y 50: 13
minimo=int(input("Introduce un numero minimo "))
print("Escribe un numero mayor que ",minimo)
maximo=int(input("Introduce un numero maximo  "))
b=maximo
flotante=minimo
lista=[]
while (maximo<minimo):
    print(minimo," no es mayor que ",maximo,"vuelve a probar ")
while (maximo>minimo):
    lista.append(minimo)
    lista.append(maximo)
    print("Escribe un numero entre ",minimo," y ",maximo,end=" ")
    flotante=int(input())
    while flotante>minimo and flotante<maximo:
        lista.append(flotante)
        flotante=(int(input("introduce otro numero ")))
    maximo=minimo
print("Los numeros escritos entre ",minimo," y ",b," son ", lista)
