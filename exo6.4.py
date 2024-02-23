def ordreCroissant(a,b) : #fonction permettant de remettre dans l'ordre les nombres input par l'utilisateur
    if a > b :
        return b,a
    
    if b > a :
        return a,b

def sommeEntiers(a,b) : #fait la dite somme

    petit,grand = ordreCroissant(a,b)
    res = petit

    for i in range(petit+1,grand+1,1) : #parcours la liste en incrementant le plus petit nombre jusqu'au plus grand en faisant la somme à chaque fois 

        res = res + i
    
    return res

a = int(input("A ? "))
b = int(input("B ? "))
petit,grand = ordreCroissant(a,b)

print("La somme des entiers de",petit,"à",grand,"est",sommeEntiers(a,b)) #affiche le résultat
