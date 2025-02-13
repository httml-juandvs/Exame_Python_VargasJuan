import json
def abrirJSON():
    dicFinal={}
    with open('./bbdd_Fut.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd_Fut.json",'w') as outFile:
        json.dump(dic,outFile)
    
admin={}

booleanito = True
while(booleanito==True):
    
    print("--------------------------------")
    print("¿A que equipo te gustaria ingresar?")
    print("1. Admin")
    print("2. Usuario")
    print("3. Registrarse")
    print("4. Cerrar programa")
    opt=input(":")
    ##Leer archivo JSON y pasarlo a dic
    admin=abrirJSON()
    if(opt=="1"):
        print("¿Qué te gustaría hacer adentro de Admin")
        print("1.Ver Usuarios")
        print("2.Agregar uno nuevo")
        print("3.Modificar uno")
        print("4.Eliminar uno")
        opt3=int(input(":"))
        if(opt3==1):
            print("-----------------------------")
            print("--------Usuarios--------")
            print("------------------------")
            for i in range(len(admin[opt]["usuarios"])):
                print(admin[opt]["usuarios"][i])
                print("------------------------")
        elif(opt3==2):
            nuevoUser=input("¿Como se llama el nuevo User?:")
            admin[opt]["usuarios"].append(nuevoUser)
                #Guardar diccionario en el archivo JSON
            guardarJSON(admin)
            print("Usuario agregado")
    elif(opt=="4"):
        booleanito = False
        break
