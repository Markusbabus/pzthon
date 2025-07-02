import sys

while True:
    print('Mi a Felhasználónév?')
    Fnev = input()

    if Fnev != 'Márk':
        print('Rossz Felhasználónév')
        continue

    print('Helyes Felhasználónév')

    for n in range(3, -1, -1) :
        print('Mi a jelszó?')
        Jszó = input()

        if Jszó == 'M1027' :
            print('Sikeres belépés')
            sys.exit()

        elif n !=0 :
            print('Sikertelen belépés, még ' + str(n) + ' próbája van')

        else:
            print('Sikertelen belépés')
            Fnev = ''
            continue