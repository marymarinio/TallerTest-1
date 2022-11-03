ingresarPlaca=input("ingrese la placa Boliviana de  a verificar: ")
numeroCaracteres =len(ingresarPlaca)
numero=['1','2','3','4','5','6','7','8','9','0']
simbolos=[" ","-"]
letrasMayusculas=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
contadorPrimerosDigitos=0
simbolosNoPermitido=['@','#',',']
if(numeroCaracteres>=7 & numeroCaracteres<=8):
    for i in range (0,numeroCaracteres):
        if(contadorPrimerosDigitos >= 3):
            if((ingresarPlaca[i] in numero)or(ingresarPlaca[i] in letrasMayusculas) or (ingresarPlaca[i] in simbolos)):
                contadorPrimerosDigitos=contadorPrimerosDigitos+1
                if(contadorPrimerosDigitos==(numeroCaracteres)):
                    print("Placa Valida")
                    print("'"+ingresarPlaca+"'")
                    break
            else:
                print("placa invalida")
                if (ingresarPlaca[i] in simbolosNoPermitido):
                    print("Error simbolos no permitidos @,#,.")
                    print("usted ingreso un caracter prohivido que es"+"'"+ingresarPlaca[i]+"'")
                    break
                elif(ingresarPlaca[i] not in letrasMayusculas):
                    print('las letras deben estar en Mayusculas por favor ingrese de nuevo pero con las letras en mayusculas')
                    break
                else:
                    print("usted ingreso un caracter no permitido "+"'"+ingresarPlaca[i]+"'") 
                    break
        if(contadorPrimerosDigitos<3):
            if(ingresarPlaca[i] in numero):
                contadorPrimerosDigitos=contadorPrimerosDigitos+1
        elif(contadorPrimerosDigitos==0):
            
            print('Error en la parte inicial: la placa debe empezar con 3 digitos de tipo numerico')
            print("Caracter no indentificado: "+ "'"+ingresarPlaca[i]+"'"+" invalido")
else:
    print('muy pocos caracteres minimamente deben ser 7 segun lo que vi la hoja')    