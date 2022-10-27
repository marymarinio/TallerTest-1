nroDeFilasPorTeclado = int(input("Ingrese un Nro: "))

for cadaFila in range(nroDeFilasPorTeclado):
    for cadaColumna in range(cadaFila+2):
        print(cadaColumna+2, end=",")
    print("\n")