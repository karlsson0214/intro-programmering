def max(a, b):
    if a > b:
        return a
    else:
        return b
    
def triangel(a, b, c):
    # trubbig en > 90, rätvinklig 90, spetsig ingen > 90
    störst_vinkel = max(max(a, b), c)
    if a + b + c != 180:
        print("Det är inte en triangel")
    elif störst_vinkel > 90:
        print("Trubbig triangel")
    elif störst_vinkel == 90:
        print("Rätvinklig triangel")
    else:
        print("Spetsig triangel")



triangel(2, 2, 2)
triangel(90, 45, 45)
triangel(100, 40, 40) # trubbig
triangel(80, 50, 50) # spetsig