# Det som visas efter hashtag (#) nedan är det som
# skrivs ut av print

lista = [1, 3, 3, 4, 3, 6, 3, 2]

antalTreor = 0
for tal in lista:
    if (tal == 3):
        antalTreor = antalTreor + 1
print("antal treor: ", antalTreor)
#antal treor:  4

print("count antal 3:", lista.count(3))

for i in range(2, 10):
    print(lista[i])
