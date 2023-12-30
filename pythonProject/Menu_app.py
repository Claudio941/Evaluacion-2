compras=[]

def agregar_compra ():
    compra = int(input("Ingrese el monto de la compra :  "))
    compras.append(compra)
def mostrar_compra():
    print ("compras :")
    for i in compras:
        print("${0:5.2f}".format(i))


def mostrar_total():
    total_gastado = sum(compras)
    print("El total gastado es :")
    print("${0:5.2f}".format(total_gastado))

while True:
    print("1. Agregar Compra")
    print("2. Mostrar Compra")
    print("3. Mostrar total gastado")
    print("4. salir")
    opcion = int(input("Seleccione una opción :  "))
    if opcion == 1:
          agregar_compra()
    if opcion == 2:
          mostrar_compra()
    if opcion == 3:
            mostrar_total()
    if opcion == 4:
         print("Hasta luego")
         exit()



