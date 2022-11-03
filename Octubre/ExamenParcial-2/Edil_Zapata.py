def verificar():
    placa = input("Placa: ").upper()
    lista = []
    contador = 0
    letra = 0
    abc = ["A","B","C","D","E","F","G","H","I","J","K","L","Ñ","N","O","P","Q","R","S","T","U","W","Y","Z"]
    for i in placa:
        lista.append(i)
        contador+=1
        for i in lista:
            if i in abc:
                letra +=1
        
        if len(lista) <= 8 :
            return True

valido = verificar()
if valido:
    print("placa Valido")
else:
    print("placa invalida...")

    
#while True
#    if PlacaValida==True:
#        print("Placa correcta")
 #   else:
  #      print("la placa no existe")