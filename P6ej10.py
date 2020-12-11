# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, 
# el programa entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa 
# entenderá que no quieres introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene 
# esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
# Dame un nombre: Héctor Quiroga
# Escribe una nota: 4
# Escribe otra nota: 8.5
# Escribe otra nota: 12
# Dame otro nombre: Inés Valls
# Escribe una nota: 7.5
# Escribe otra nota: 1
# Escribe otra nota: 2
# Escribe otra nota: -5
# Dame otro nombre:
# Las notas de los alumnos son:
# Héctor Quiroga: 4.0 - 8.5
# Inés Valls: 7.5 - 1.0 - 2.0
lista=[]
auxiliar=[]
nombre="A"
while(nombre!=""):
    nombre=input("Dame un nombre: ")
    if(nombre!=""):
        lista.append(nombre)
        nota=float(input("Dame una nota: "))
        while nota>=0 and nota<=10:
            lista.append(nota)
            nota=float(input("Dame una nota: "))
        auxiliar.append(lista)
        lista=[]
print("Las notas de los alumnos son: ")#por ahora he llegado hasta aqui, me falta averiguar el print
for i in range(len(auxiliar)):
    print(auxiliar[i][0],": ",end="")
    for j in range(1,len(auxiliar[i])):
        print(" - ",auxiliar[i][j],end=" ")
    print("\n")
print("finalizado")