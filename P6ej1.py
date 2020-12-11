# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
# Escribe una palabra: viaje
# Escribe más palabras: aventura
# Escribe más palabras: cómic
# Escribe más palabras:
# Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']
masPalabras=str(input("Introduce una palabra "))
lista=[]
while (masPalabras!=""):
    lista.append(masPalabras)
    masPalabras=str(input("Introduce otra palabra "))
print (lista)