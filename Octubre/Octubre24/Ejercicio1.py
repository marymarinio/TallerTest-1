#Ejercicio media piramire acendente
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
nroDeFilasPorTeclado = int(input("Ingrese un Nro: "))

for cadaFila in range(nroDeFilasPorTeclado, 0, -1):
    for cadaColumna in range(1, cadaFila+1):
<<<<<<< HEAD
        print(cadaColumna, end="")
=======
        print(cadaColumna, end="*")
>>>>>>> 7f4a11fefabcabe8c6752cfa1219c0f9a15cb767
    
    print("\n")
