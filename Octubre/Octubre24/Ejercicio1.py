from audioop import mul

nroDeFilasPorTeclado = int(input("Ingrese un Nro: "))

for cadaFila in range(nroDeFilasPorTeclado, 0, -1):
    for cadaColumna in range(1, cadaFila+1):
        print(cadaColumna, end=" ")
    
    print("\n")
print("Esta solucion muy buena pero...")
for multiplicar in range(nroDeFilasPorTeclado):
    for num in range(nroDeFilasPorTeclado):
        resul=+num
        print(resul,"Jelouda")
