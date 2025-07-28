import app

def convertidor_txt():
    nota = 1
    with open('notas.txt', 'w') as archivo:
        for clave, valor in app.notas.items():

            archivo.write(f"--- Nota {nota} ---\n Titulo: {clave}: \n {valor}\n")
            nota +=1
convertidor_txt()
