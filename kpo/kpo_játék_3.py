import random, sys

print('KŐ, PAPÍR, OLLÓ')

nyerések = 0
vesztések = 0
döntetlenek = 0

def game():
    global nyerések, vesztések, döntetlenek
    if lépés == comp_l:
        print('Döntetlen!')
        döntetlenek = döntetlenek + 1

    elif (lépés == 'k' and comp_l == 'o') or (lépés == 'p' and comp_l == 'k') or (lépés == 'o' and comp_l == 'p'):
        print('Nyertél!')
        nyerések = nyerések + 1

    elif (lépés == 'k' and comp_l == 'p') or (lépés == 'p' and comp_l == 'o') or (lépés == 'o' and comp_l == 'k'):
        print('Vesztettél!')
        vesztések = vesztések + 1

while True:
    print('%s Nyerések, %s Vesztések %s Döntetlenek' %(nyerések, vesztések, döntetlenek) )

    while True:
        print('Írd be a lépésed: (k)ő (p)apír (o)lló vagy (ki)lépés ')
        lépés = input()
        if lépés == 'ki':
            sys.exit()

        if lépés == 'k' or lépés == 'p' or lépés == 'o':
            break

        print('Írj k-, p-, o-, vagy ki-t.')


    if lépés == 'k':
        print('KŐ vs' , end=' ')

    elif lépés == 'p':
        print('PAPÍR vs', end=' ')

    elif lépés == 'o':
        print('OLLÓ vs', end=' ')


    rnumb = random.randint(1, 3)

    if rnumb == 1:
        comp_l = 'k'
        print('KŐ')

    elif rnumb == 2:
        comp_l = 'p'
        print('PAPÍR')

    elif rnumb == 3:
        comp_l = 'o'
        print('OLLÓ')


    game()