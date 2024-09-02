def ordreCroissant(a,b) :
    return min(a,b), max(a,b)

def sommeEntiers(a,b) :

    petit,grand = ordreCroissant(a,b)
    res = petit

    for i in range(petit+1,grand+1,1) :

        res = res + i
    
    return res

a = int(input("A ? "))
b = int(input("B ? "))
petit,grand = ordreCroissant(a,b)

print("La somme des entiers de",petit,"à",grand,"est",sommeEntiers(a,b))
