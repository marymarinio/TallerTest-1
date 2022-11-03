print("=== Validador de Placa ====")
print("OJO -.- que no contenga estos simbolos .(punto) - @(arroba) - #(numeral))")
placa = input("Ingrese Placa: ").upper()
tamanioplaca = len(placa)
placalista = list(placa)

numeros = ['1','2','3','4','5','6','7','8','9','0']
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','-']

if tamanioplaca <= 6:
    placalista.append(" ")
    placalista.append(" ")

if tamanioplaca <= 8:
    try:
        if placalista[0] in numeros and placalista[1] in numeros and placalista[2] in numeros and (placalista[3] in letras or placalista[3] in numeros) and placalista[4] in letras and placalista[5] in letras or (placalista[6] in letras and placa[7] in letras):
            print("=== Placa ",placa," Valida ===")
        else:
            print("=== Placa ",placa," Invalida ===")
    except:
        print("=== Placa ",placa," Invalida ===")
else:
    print("=== Placa ",placa," Invalida ===\nPor sobrepasarse del tamaño de placa permitido")