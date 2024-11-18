#Det som visas efter hashtag (#) nedan är det som
#skrivs ut av print

inköpslista = ["bröd", "smör", "ost"]
print(inköpslista)
#['bröd', 'smör', 'ost']

### index: 0, 1, 2, ... och -1, -2, ...
 
print("element vid index 0: ", inköpslista[0])
#element vid index 0:  bröd

print("element vid index 1: ", inköpslista[1])
#element vid index 1:  smör

print("element vid index 2: ", inköpslista[2])
#element vid index 2:  ost

print("från slutet med negativa index")
#från slutet med negativa index

print("element vid index -1: ", inköpslista[-1])
#element vid index -1:  ost

print("element vid index -2: ", inköpslista[-2])
#element vid index -2:  smör

print("element vid index -3: ", inköpslista[-3])
#element vid index -3:  bröd

### listans längd - len()

print("antal element i listan: ", len(inköpslista))
#antal element i listan:  3

### lägg till element i listan - append()

inköpslista.append("fil")
print(inköpslista)
#['bröd', 'smör', 'ost', 'fil']

### lägg till lista på slutet av listan - extend()

inköpslista.extend(["tomat", "gurka"])
print(inköpslista)
#['bröd', 'smör', 'ost', 'fil', 'tomat', 'gurka']

### sätt in element på given plats - insert()

inköpslista.insert(1, "skorpor")
print(inköpslista)
#['bröd', 'skorpor', 'smör', 'ost', 'fil', 'tomat', 'gurka']

### ta bort givet element - remove()

inköpslista.remove("fil")
print(inköpslista)
#['bröd', 'skorpor', 'smör', 'ost', 'tomat', 'gurka']

### Överkurs nu: Om "fil" finns på flera ställen i listan tas bara den första förekomsten bort.
### ta bort och returnera sista elementet - pop()

last = inköpslista.pop()
print("last removed: ", last)
#last removed:  gurka

print(inköpslista)
#['bröd', 'skorpor', 'smör', 'ost', 'tomat']

#### ta bort och returnera valfritt element - pop(0)

first = inköpslista.pop(0)
print("first removed: ", first)
#first removed:  bröd

print(inköpslista)
#['skorpor', 'smör', 'ost', 'tomat']

### sortera - sort()

inköpslista.sort()
print("sorterad: ", inköpslista)
#sorterad:  ['ost', 'skorpor', 'smör', 'tomat']

### omvänd ordning

inköpslista.reverse()
print("omvänd ordning: ", inköpslista)
#omvänd sortering:  ['tomat', 'smör', 'skorpor', 'ost']

### elements index - index()

print("skorpor har index:", inköpslista.index('skorpor'))
#skorpor har index: 2

### finns ett element i listan? - in

if 'skorpor' in inköpslista:
    print('skorpor på listan')
else:
    print('skorpor saknas på listan')

#skorpor på listan
