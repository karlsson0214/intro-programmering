import random

spela_igen = "j"
while spela_igen == "j":
    tal = random.randint(1, 6)
    print(tal)
    if tal == 1:
        print("ett")
        print("ett")
    elif tal == 2:
        print("två")
    elif tal == 3:
        print("tre")
    else:
        print("fyra eller högre")
    spela_igen = input("Vill du spela igen? (j/n) ")    