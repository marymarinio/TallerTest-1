numeros=["0","1","2","3","4","5","6","7","8","9"]
digitosNoValidos=[".","#","@"]
placa=input("Ingrese la placa: ")
valor=0
c=0
for contador in placa:
    if len(placa)<=8:
        if contador in digitosNoValidos:
            print("Contiene un digito invalido: ",contador)
            valor=1
            break
        else:
            if c<=2:
                if contador not in numeros:
                    print("digito incorrecto, los primeros 3 digitos deben ser numeros ")
                    valor=1
                    break
    else:
        print("El numero de digitos en la placa es incorrecto ")
        valor=1
        break
    c=c+1
if valor == 0:
    print("la placa ",placa," es correcta")
else:
    print("la placa ",placa," es incorrecta")
