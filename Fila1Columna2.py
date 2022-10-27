#Josue Guzman Espejo
#Facundo Miranda Yucra
#Salomon Mena Lazarte
numero=int(input("ingrese un numero: "))
ListaNumeros=[]
contador=0
while contador<numero:
    contador=contador+1
    ListaNumeros.append(str(contador))
    EliminarCorchete=" ".join(ListaNumeros)
    print(EliminarCorchete)