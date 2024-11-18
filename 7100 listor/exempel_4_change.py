import random

tärningar = []

for i in range(20):
    # lägg till slumptal, 1 till 4, i listan tärningar
    tärningar.append(random.randint(1,4))

print(tärningar)
print("min", min(tärningar))
print("max", max(tärningar))
print("summa", sum(tärningar))
print("antal fyror", tärningar.count(4))

# räkna antal ettor
antal_ettor = 0
for tärning in tärningar:
    if tärning == 1:
        antal_ettor = antal_ettor + 1

print("antal ettor", antal_ettor)

# fungerar inte om vi vill ändra på värden i listan
for tärning in tärningar:
    tärning = 5 - tärning

print(tärningar)

# alternaitv 1
# ändra på värden i listan
# invertera listan: 1 <--> 4 och 2 <--> 3
for i in range(len(tärningar)):
    tärningar[i] = 5 - tärningar[i]

print(tärningar)

# alternativ 2
i = 0
for tärning in tärningar:
    tärningar[i] = 5 - tärning
    i = i + 1

print(tärningar)
