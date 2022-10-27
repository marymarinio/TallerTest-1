#Marcos Blazquez 
#Kelly Arenas
#Lizeth Aduviri
listas=int(input("Ingrese numero:"))
lista=[]

for i in range(1,listas+1):
    lista.append(i)
print(lista)
lista1=[]
for f in range(1,listas):
    lista1.append(f)

print(lista1)

lista2=[]
for g in range(1,listas):
    lista2.append(g)
lista2.remove(2)
print(lista2)

