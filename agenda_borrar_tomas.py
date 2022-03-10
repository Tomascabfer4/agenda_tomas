###Parte de agenda Tomás Cabello Fernández,10/03/2022###
###Función borrar###
###Está función te pide un nombre, si le das un contacto existente,###
###te responde pidiendote el pulsado de la tecla s para confirmar el borrado###
###Si no existe el contacto simplemente el programa responde diciendo que no existe.###  
def borrar_Tcabello(nombre,agenda):
    nombre = input("Nombre del contacto a borrar: ")
    if nombre in agenda:
        opcion = input("Pulsa 's' si quieres borrarlo. Otra tecla para continuar.")
        if opcion == "s":
            del agenda[nombre]
    else:
        print("No existe el contacto.")



