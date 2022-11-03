def Placa():
    lista=[]
    numeroPlaca=input("ingrese numero de placa:")
    contador=0
    caracteres=". @ #"
    numeros=("0 1 2 3 4 5 6 7 8 9")
    Abcedario=("A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z")
    abecedario=Abcedario.lower()
    for num in numeroPlaca:
        contador+=1
    for tamanio in numeroPlaca:
        lista.append(tamanio)
    for verificar in caracteres:
        if verificar in lista:
            print("placa no valida")
    if contador >=9:
        print("placa no valida")
    numPlaca=numeroPlaca[:4]
    if numPlaca in abecedario:
        print("no debe ir letras depues de 4 digitos ")
    else:
        print("si es valido")
    letrasPla=numeroPlaca[3:]
    if letrasPla in abecedario:
        print("no debe ir letras al inicio")
    else:
        print("si es valido")
Placa()