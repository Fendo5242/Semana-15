from datetime import datetime 
ahora = datetime.now()
fecha = ahora.strftime("%d/%m/%Y")
archivo= open ("ventas.txt" , "a")
TOTAL = 0 


def obtenerIGV(a):
    subTotal = a * 0.18
    return subTotal
def obtenerIGVTotal(a):
    subTotal = a * 1.18
    return subTotal
def obtenerTotal(a,b):
    total = a+b
    return total
print("ventas diarias: ")
print("-"*30)

a = int(input("Ingresa la cantidad de productos: "))
for x in range (0,a):
    producto = str(input("Ingresa producto: "))
    precio = str(input("Ingresa precio: "))
    cantidad = str(input("Ingresa cantidad: "))
    archivo.write(cantidad+ "\t" + producto + "\t" + precio + "\n")
    TOTAL = TOTAL + obtenerTotal(int(precio), int(cantidad))


archivo.write("Fecha: " + str(fecha) + "\n")
archivo.write("Subtotal: " + str(TOTAL) + "\n")
archivo.write("IGV: " + str(obtenerIGV(TOTAL)) + "\n")
archivo.write("Total: " + str(obtenerIGVTotal(TOTAL)) + "\n")
archivo.close()
