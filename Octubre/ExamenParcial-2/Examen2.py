placaIngresada =str(input("Placa: "))

analisisPlaca = list(placaIngresada)
numeros = str([0,1,2,3,4,5,6,7,8,9])
letras = ['A','B','C','D','E','F','G','H','I','J','K','L',
        'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if len(analisisPlaca) <= 8 and len(analisisPlaca) >=6:
    if analisisPlaca[0] in numeros and analisisPlaca[1] in numeros and analisisPlaca[2] in numeros :
        if analisisPlaca[-1] in letras and analisisPlaca[-2] in letras and analisisPlaca[-3] in letras:
            if ('.' or '@' or '#') in analisisPlaca:
                print('Caracteres invalidos detectados')        
            else:
                if ((analisisPlaca[3] in numeros) or (analisisPlaca[3] in letras) or analisisPlaca[3] == '-' or analisisPlaca[3] == ' ') and ((analisisPlaca[4] in numeros) or (analisisPlaca[4] in letras) or analisisPlaca[4] == '-' or analisisPlaca[4] == ' '):
                    print('Valido')
                else:
                    print('Invalido caracteres desconocidos')
        else:
            print('Invalido no sigue la secuencia correcta')
    else:
        print('Invalido no sigue la secuencia correcta')
else:
    print('Placa no tiene el tamaño requerido')
