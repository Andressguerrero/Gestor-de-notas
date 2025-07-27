from datetime import  date
import json
fecha = date.today().isoformat() 
notas = {}

while True:
    print("Bienvenido Gestor de notas\n" \
    "¿que desea hacer el dia de hoy?")
    print("1. Resgistrar una nota:")
    print("2. Mostrar todas notas: ")
    print("3. buscar una nota:")
    print("4. Eliminar una nota:")
    print("5. importar notas en .txt:")
    opcion = int(input("ingresa una opcion:"))

    def registrar_notas ():
        titulo = input("ingresa un Titulo:")
        contenido = input("ingresa el contenido:")
        #fecha = ("27/07/2025")
        notas ["titulo"] = titulo
        notas ["fecha"] = fecha 
        notas ["contenido"] = contenido 
        print(notas)

    def buscar_notas ():
        print("para buscar una nota tienes que ingresa el titulo")
        buscar = input("ingresa el titulo de la nota:")
        buscar_nota = notas.get(buscar)
        print(buscar_nota)
        
    def eliminar_nota ():
        print("para eliminar una nota tienes que ingresa el titulo")
        eliminar = input("ingresa el titulo de la nota:")
        eliminar_notas = notas.pop(eliminar)
        print(notas)

    def convertidor_txt():
        with open('notas.json', 'r') as archivo:
            notas = json.load(archivo)
            print(notas)

            
    if opcion == 1:
        registrar_notas()
    elif opcion == 2:
        print("notas registradas:\n",
               notas)
    elif opcion == 3:
        buscar_notas ()
    elif opcion == 4:
        eliminar_nota ()
    elif opcion == 5:
        convertidor_txt()

        
