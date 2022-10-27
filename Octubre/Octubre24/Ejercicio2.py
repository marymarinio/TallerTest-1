nroDeFilasPorTeclado = int(input("Ingrese un Nro: "))

for cadaFila in range(nroDeFilasPorTeclado):
    for cadaColumna in range(cadaFila+1):
        print(cadaColumna+1, end="/")
    print("\n")
