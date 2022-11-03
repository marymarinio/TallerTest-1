aux3 = 0
aux2 = 0
placanum = input("Ingrese los caracteres de su placa: ")

aux = ""
for aux in placanum:
    aux2 += 1
    #Validando que en los primeros 3 o 4 digitos sean numeros
    if aux  == "1" or aux == "2" or aux == "3" or aux == "4" or aux == "5" or aux == "6" or aux == "7" or aux == "8" or aux == "9" or aux == "-":
        print(aux)
    else:
        print("por favor los primero digitos deben ser numericos")
        break
#Validando que la cantidad no sobre pase los 9 y no baje de los 7
if aux2 > 6 and aux2 <= 9:
    print("Placa Boliviana")
else:
    print("La placa boliviana solo tiene 8 digitos por favor vuelva a intentar")






