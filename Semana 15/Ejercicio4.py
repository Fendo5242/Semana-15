print("Bienvenido a este pequeño menú")


opcion = input("¿Desea escribir o leer (E/L) ")
if opcion == "E":
        texto = input("Escribe un texto: ")
        file = open ("texto.txt", "w")
        file.write("Texto: " + texto )
else:
        file = open ("texto.txt", "r")
        print (file.read())
