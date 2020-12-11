# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de 
# los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
# Escribe límite: 50
# Escribe un valor: 10
# Escribe otro valor: 25
# Escribe otro valor: 7
# Escribe otro valor: 14
# El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
limite=int(input("Introduce un numero limite "))
sumador=int(input("Introduce un valor: "))
numero=sumador
lista=[sumador]
while numero<limite:
    sumador=int(input("Introduce otro valor :"))
    numero = numero+sumador
    lista.append(sumador)
print("El limite a superar es ",limite,"la lista creada es ",lista," ya que la suma de estos es: ",numero)
    