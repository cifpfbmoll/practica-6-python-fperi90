# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. 
# El programa termina escribiendo los dos números tal y como se pide:
# Escribe un número: 6
# Escribe un número mayor que 6: 6
# 6 no es mayor que 6. Vuelve a introducir un número: 1
# 1 no es mayor que 6. Vuelve a introducir un número: 8
# Los números que has escrito son 6 y 8
primero=int(input("Introduce un numero "))
print("Introduce un numero mayor que",primero,": ",end="")
segundo=int(input())#aqui para evitar pasarle el "primero" como un parametro, dado que no lo acepta porque int solo 
                    #acepta un valor, he impreso mensaje en pantalla y me he cargado el salto de linea, para que parezca
                    #que continua.
while segundo==primero or segundo<primero:
    print(segundo," no es mayor que ", primero,end="")
    segundo=int(input(" Vuelve a introducir un numero "))
print("Los numeros que has escrito son ",primero,"y", segundo)
