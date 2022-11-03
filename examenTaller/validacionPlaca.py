def verificacion(placa):
    contador=0
    contadorNumeros=0
    contadorLetras=0
    verificacion=False
    listaNumeros=["1","2","3","4","5","6","7","8","9","0"]
    listaLetras=["A","B","C","D","E","F","G","H","I","J","K",
                "L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    caracteresProhibidos=False
    if len(placa)<=8:
        for letra in placa:
            if letra=='.' or letra == '@' or letra == '#':
                caracteresProhibidos=True
        if caracteresProhibidos!=True:
            for letra in placa:
                contador+=1
                if contador <5:
                    for numero in listaNumeros:
                        if letra == numero:
                            contadorNumeros+=1
                    if contadorNumeros <=4 and contadorNumeros>=3:
                        verificacion=True
                elif contador==5:
                    if letra == '-' or letra == ' ':
                        verificacion=True
                elif contador>5:
                    for abecedario in listaLetras:
                        if letra==abecedario:
                            contadorLetras+=1
                    if contadorLetras == 3:
                        verificacion=True

            if verificacion==True:
                print("Placa valida")
            else:
                print("Placa invalida")
        else:
            print("existe un caracter prohibido")
    else: 
        print("la placa sobrepasa los 8 caracteres ")

placa=input("Ingrese una placa: ")
placa=placa.upper()
verificacion(placa)



