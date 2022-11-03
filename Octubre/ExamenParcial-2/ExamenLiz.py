#parcial
def validacionPlacas():
    opcion=0
    while opcion!=1:
        #1ER REQUERIMIENTO
        print("""       VALIDACION DE PLACAS DEL TERRITORIO NACIONAL BOLIVIANO""")
        
        placa=input("Ingrese la placa de su auto:")
        placa=placa.upper()
        placa1=[]
        for i in placa:
            placa1.append(i)
        placa=len(placa)
        if placa1[0]=="A"or placa>8 or placa1[1]=="A" or placa>8 or placa1[2]=="A":
            print("PLACA INVALIDA")
        else:
            if placa1 != "." or "@" or "#":
                print("PLACA VALIDA")
            else:
                print("Placa invalida")
        input()
validacionPlacas()