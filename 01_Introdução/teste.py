from random import random, randint



def caracoroa():
    a = random()
    print(a)

    if a >= 0.5:
        return 'Cara'
    else:
        return 'Coroa'
    
 
print(f'O resultado deu {caracoroa()}')
