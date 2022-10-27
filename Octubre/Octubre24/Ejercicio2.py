#Ejercicio media piramire decendente
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
nroDeFilasPorTeclado = int(input("Ingrese un Nro: "))

for cadaFila in range(nroDeFilasPorTeclado):
    for cadaColumna in range(cadaFila+1):
        print(cadaColumna+1, end="*")
    print("\n")
