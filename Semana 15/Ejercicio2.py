from datetime import datetime


nombre = input("Ingrese su nombre: ")
nota_1 = int(input("Ingrese la nota 1: "))
nota_2 = int(input("Ingrese la nota 2: "))


promedio = (nota_1 + nota_2)/2

aprobado = False

ahora = datetime.now()


if promedio >= 13:
    aprobado = True


file = open ("notas.txt", "w")
file.write("Nombre: " + nombre + "\n")
file.write("Nota_1: " + str(nota_1) + "\n")
file.write("Nota_2: " + str(nota_2) + "\n")
file.write("Promedio: " + str(promedio) + "\n")
file.write("Aprobado: " + str(aprobado) + "\n")
fecha = ahora.strftime("%Y/%m/%d")
file.write("La fecha actual es: " + fecha)
file.close()
