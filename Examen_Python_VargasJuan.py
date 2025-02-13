import json
def abrirJSON():
    dicFinal={}
    with open(f"./movistar.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open(f"./movistar.json",'w') as outFile:
        json.dump(dic,outFile)
nuevoUser={}
nuevoUser=abrirJSON
def aggUser():
    print("")
    print("")
    print("  |     Ingrese los siguietes datos:      |")
    num =int(input("  |  1. Numero de telefono               |"))
    ##nombre=input(("  |  2. Nombre                           |"))
    ##apellido=input(("  |  3. Apellido                         |"))
    print("  | USUARIO REGISTRADO CON EXITO         |")
    nuevoUser["movistar"].append(num)
    ##for i in range(len(aggUser)("movistar")["usuarioNuevo"].append(num)

    guardarJSON(nuevoUser)