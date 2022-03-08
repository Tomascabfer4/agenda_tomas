agenda = {}
def mostrarmenu():
    print("|-----------------------------------------|")
    print("|   :: AGENDA TOMÁS CABELLO FERNÁNDEZ ::  |")
    print("|-----------------------------------------|")
    print("|                                         |")
    print("|  1. Añadir/modificar                    |")
    print("|  2. Buscar                              |")
    print("|  3. Borrar                              |")
    print("|  4. Listar                              |")
    print("|  5. Salir                               |")
    print("|_________________________________________|")
    print("")
    x = input ("Dime la función a realizar: ")
    opc = int (x)
    return (opc)

def borrarTcabello():
    nombre = input("Nombre del contacto a borrar: ")
    if nombre in agenda:
        opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
        if opcion == "s":
            del agenda[nombre]
    else:
        print("No existe el contacto.")

###Programa###
seleccion = mostrarmenu()
if (seleccion<0 or seleccion>4):
    print("La opción es incorrecta.")

while (seleccion>0 and seleccion<5):
    if (seleccion==3):
        borrarTcabello()
    #elif

    seleccion = mostrarmenu()


