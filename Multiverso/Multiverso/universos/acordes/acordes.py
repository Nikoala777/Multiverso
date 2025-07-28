import random

def gen_tetrachords_random(top=6):
    intervalos = {'st':1, 'T':2, 'T1/2':3}
    suma = 0
    tetracorde = []
    while suma <5:
        intervalo= random.choice(list(intervalos.keys()))
        suma += intervalos[intervalo]
        
        if intervalos[intervalo] == 3 and random.randint(0, 9) > 3:
            suma -= intervalos[intervalo]
        elif intervalos[intervalo] == 1 and random.randint(0, 9) > 5:
            suma -= intervalos[intervalo]
        elif suma > top:
            suma -= intervalos[intervalo] 
        elif len(tetracorde) == 3 and suma < 5:
            suma -= intervalos[intervalo]
        else:
            tetracorde.append(intervalo)
    return tetracorde