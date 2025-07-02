import sys

print('KŐ, PAPÍR, OLLÓ')

nyerések = 0
vesztések = 0
döntetlenek = 0

while True:
    print('%s Első Játékos Nyerések, %s Második Játékos Nyerések %s Döntetlenek' %(nyerések, vesztések, döntetlenek) )

    while True:
        print(' ELSŐ JÁTÉKOS: Írd be a lépésed: (k)ő (p)apír (o)lló vagy (ki)lépés ')
        lépés_1 = input()

        if lépés_1 == 'ki':
            sys.exit()

        print(' MÁSODIK JÁTÉKOS: Írd be a lépésed: (k)ő (p)apír (o)lló vagy (ki)lépés ')
        lépés_2 = input()

        if lépés_2 == 'ki':
            sys.exit()

        if (lépés_1 == 'k' or lépés_1 == 'p' or lépés_1 == 'o') and ( lépés_2 == 'k' or lépés_2 == 'p' or lépés_2 == 'o'):
            break

        print('Írj k-, p-, o-, vagy ki-t.')


    if lépés_1 == lépés_2:
        print('Döntetlen!')
        döntetlenek = döntetlenek + 1

    elif lépés_1 == 'k' and lépés_2 == 'o':
        print('Az Első Játékos Nyert!')
        nyerések = nyerések + 1

    elif lépés_1 == 'p' and lépés_2 == 'k':
        print('Az Első Játékos Nyert!')
        nyerések = nyerések + 1

    elif lépés_1 == 'o' and lépés_2 == 'p':
        print('Az Első Játékos Nyert!')
        nyerések = nyerések + 1

    elif lépés_1 == 'k' and lépés_2 == 'p':
        print('A Második Játékos Nyert!')
        vesztések = vesztések + 1

    elif lépés_1 == 'p' and lépés_2 == 'o':
        print('A Második Játékos Nyert!')
        vesztések = vesztések + 1

    elif lépés_1 == 'o' and lépés_2 == 'k':
        print('A Második Játékos Nyert!')
        vesztések = vesztések