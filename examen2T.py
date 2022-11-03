
def validar(placa):
    lista_placa = []
    for i in placa:
        lista_placa.append(i)
    
    if len(lista_placa) <=8:
        try:
            contador = 0
            letra = 0
            alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-']
            no_validos=['.','@','#',]
            for i in lista_placa:
                contador +=1          
        except:
            pass
        
        if contador >=3:
            for i in lista_placa:
                if i in alfabeto:
                    letra +=1
            for i in lista_placa:
                if i in no_validos:
                    letra-=1
            if letra == 3:
                return True
            else:
                return True
        else: 
            return True  
    else:
        return True

while True:
    placa = input("Ingrese placa del vehiculo: ").upper()
    print('Su placa es: ',placa)
    valido = validar(placa)
    if valido:
        print("placa Valido")
        break
    else:
        print("placa no valido.. Por favor intente Nuevamente ")