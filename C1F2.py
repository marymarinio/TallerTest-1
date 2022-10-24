#numero=int(input("Ingrese un numero: ")) #3
valor=3
lista=[]
numeroinicial=1
for numero in range(1,valor+1):
    lista.append(numero)
for i in range(len(lista)):
    for j in range(numeroinicial):
        print(lista[j],end="")
    numeroinicial+=1
    print("\n")
