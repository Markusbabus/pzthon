Fnev = ''
n = 0

while Fnev != 'Márk':
    print('Mi a Felhasználónév?')
    Fnev = input()
    if Fnev != 'Márk':
        print('Rossz Felhasználónév')

if Fnev == 'Márk' :
    print('Mi a jelszó?')
    Jszó = input()

    if Jszó == 'M1027':
        print('Sikeres belépés')

    else:
        print('Sikertelen belépés')