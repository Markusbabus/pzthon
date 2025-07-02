n = 0

while True:
    print('Mi a Felhasználónév?')
    Fnev = input()

    if Fnev != 'Márk':
        print('Rossz Felhasználónév')
        continue

    print('Helyes Felhasználónév')
    break

while n != 4:
    print('Mi a jelszó?')
    Jszó = input()

    if Jszó == 'M1027':
        print('Sikeres belépés')
        break

    elif n != 4:
        n = n + 1

        if n == 4:
            print('Sikertelen belépés')
            break

        print('Sikertelen belépés, még ' + str( 4 - n ) + ' próbája van')