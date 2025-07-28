import app

def convertidor_txt():
    nota = 1
    with open('notas.txt', 'w') as archivo:
        for clave, valor in app.notas.items():
            for fecha,contenido in clave:
                nota +=1
            archivo.write(f"--- Nota {nota} ---\n Titulo: {clave}: Fecha:{fecha} \n contenido: {contenido}\n ")
convertidor_txt()
