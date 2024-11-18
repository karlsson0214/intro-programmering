# Det som visas efter hashtag (#) nedan är det som
# skrivs ut av print

skostorlek = [40, 41, 41, 42, 42, 43, 43, 43, 43, 44, 44, 45]

### minsta elementet i en lista - min()

print("min: ", min(skostorlek))
#min:  40

### största elementet i en lista - max()

print("max: ", max(skostorlek))
#max:  45

### antal element i listan - len()

print("antal: ", len(skostorlek))
#antal:  12

### summan av elementen i listan - sum()

print("summa: ", sum(skostorlek))
#summa:  511

### medel genom kombination av sum() och len()

medel = sum(skostorlek) / len(skostorlek)
print("medel: ", medel)
#medel:  42.583333333333336
