# Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de
# los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 45
# 45 es demasiado grande. Escribe otro valor: 1
# Escribe otro valor: 39
# El límite a alcanzar es 50. La lista creada es: 10, 1, 39
limite=int(input("Escribe limite "))
sumador=int(input("Escribe un valor: "))
while sumador>limite:
    print(sumador," es demasiado grande. Introduce otro numero: ",end="")
    sumador=int(input())
numero=sumador
lista=[sumador]
while numero<limite:
    sumador=int(input("Escribe otro valor: "))
    numero=numero+sumador
    while numero>limite:
        print(sumador,"es demasiado grande. Escribe otro valor: ",end="")
        numero=numero-sumador
        sumador=int(input())
        numero=numero+sumador
    lista.append(sumador)
print("El limite a alcanzar es ",limite,"la lista creada es : ",lista)
