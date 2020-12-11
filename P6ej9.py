# Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar
# debe pulsar “S” cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono.
# Nota: La lista en la que se guardan los nombres y números de teléfono tiene esta estructura[[nombre1, telef1], [nombre2, telef2], 
# [nom3, telef3], etc], es decir, lista de listas.
# Dame un nombre: Pepe González
# Dame el teléfono: 971971971
# Dame un nombre: Macarena Gómez
# Dame el teléfono: 971999999
# Dame un nombre: Pascual Ribot
# Dame el teléfono: 666555444
# Dame un nombre: S
# Los nombres y teléfonos de la agenda son:
# Pepe González: 971971971
# Macarena Gómez: 971999999
# Pasqual Ribot: 666555444
nombre=str(input("Introduce un nombre: "))
listaTotal=[(),()]
while nombre=="s":
    print("la lista esta vacia. Dame un nombre: ")
    nombre=str(input())
listaNombre =[nombre]
listaNumero =[]
flotante=0
while nombre!="s":
    numero=str(input("Introduce un numero de telefono: "))
    listaNumero.append(numero)
    print("Introduce un nombre: ",end="")
    nombre=str(input())
    flotante+=1
    listaNombre.append(nombre)
print("Los nombres y telefonos de la agenda son : ")
for i in range(flotante):
    # listaTotal.append((listaNombre[i]),listaNumero[i])
    print(listaNombre[i],": ", end="")
    print(listaNumero[i])