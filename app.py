from datetime import  date
notas = {}

def registrar_notas ():
    titulo = input("ingresa un titulo:").lower()
    while titulo in notas:
        print("Este título ya está registrado. Ingresa uno diferente.")
        titulo = input("Ingresa un título:").lower()
    contenido = input("ingresa el contenido:").lower()
    notas[titulo] = {"fecha": date.today().isoformat(), "contenido": contenido}
    todas_las_notas ()

def todas_las_notas ():
    for clave,valor in notas.items():
        print(f"{clave}:{valor}")
        
def buscar_notas ():
    print("para buscar una nota tienes que ingresa el titulo")
    buscar = input("ingresa el titulo de la nota:").lower()
    buscar_nota = notas.get(buscar)
    if buscar_nota:
        print(buscar_nota)
    else:
        print("No se encontró la nota con ese título.")


def eliminar_nota ():
    print("para eliminar una nota tienes que ingresa el titulo")
    eliminar = input("ingresa el titulo de la nota:")
    if eliminar in notas:
        notas.pop(eliminar)
        print("Nota eliminada.")
    else:
        print("Esa nota no existe.")










