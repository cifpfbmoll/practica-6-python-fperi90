# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
# Escribe una nota: 7.5
# Escribe una nota: 0
# Escribe una nota: 10
# Escribe una nota: -1
# Las notas que has Escrito son [7.5, 0.0, 10.0]
notas=float(input("Introduce una nota "))
lista=[]
while notas>0 and notas<10:
    lista.append(notas)
    notas=float(input("Introduce otra nota "))
print (lista)