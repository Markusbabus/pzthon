Jszó = ''

while True:
    print('Mi a Felhasználónév?')
    Fnev = input()

    if Fnev != 'Márk':
        print('Rossz Felhasználónév')

    if Fnev == 'Márk' and Jszó != 'M1027':
        print('Mi a jelszó?')
        Jszó = input()

        if Jszó == 'M1027':
            print('Sikeres belépés')
            break

        else:
            print('Sikertelen belépés')
            continue
