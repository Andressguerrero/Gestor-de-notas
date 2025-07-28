import app
import archivos

while True:
    try:
        print("\nBienvenido al Gestor de Notas")
        print("1. Registrar una nota")
        print("2. Mostrar todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Guardar en archivo .txt")
        print("6. Salir")

        opcion = int(input("ingresa una opcion:"))

        if opcion == 1:
            app.registrar_notas()
        elif opcion == 2:
            app.todas_las_notas ()
        elif opcion == 3:
            app.buscar_notas ()
        elif opcion == 4:
            app.eliminar_nota ()
        elif opcion == 5:
            archivos.convertidor_txt()
        elif opcion ==6:
            print("gracias por utilizar la app")
            break
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except KeyError:
        print("Error: la nota que desea eliminar, no existe")
