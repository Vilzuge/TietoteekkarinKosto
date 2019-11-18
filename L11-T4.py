tiedosto = input("anan nimi:")
f = open(tiedosto,"r")
lista = f.read().split("\n")
f.close


for i in range(0, len(lista) - 2):
    for j in range(i+1, len(lista)-1):
        if lista[i] > lista[j]:
            apu = lista[j]
            lista[j] = lista[i]
            lista[i] = apu
for rivi in lista:
    print(rivi)