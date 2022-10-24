numero=int(input("ingrese un numero: "))
ListaNumeros=[]
contador=0
while contador<numero:
    contador=contador+1
    ListaNumeros.append(str(contador))
    cadena="".join(ListaNumeros)
    print(cadena)