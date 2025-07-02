bdays = {'Márk' : 'Oct 27', 'Máté': 'Apr 25', 'Apa': 'Dec 21', 'Anya': 'Sep 28'}

while True:
    print('Írj be egy nevet! (vagy semmit hogy kilépj)')
    name = input()

    if name == '':
        break

    if name in bdays:
        print( name + ' születésnapja: ' + bdays[name])

    else:
        print('Nincs információm ' + name + ' nevű emberről')
        print('Hozzá akarod adni a listához? (y/n)')

        while True:
            ansn = input()

            if ansn not in ('y', 'n'):
                print('y/n')
                continue

            elif ansn == 'n':
                break

            else:

                print('Mi a születésnapja?')
                bdayinp = input()

                bdays[name] = bdayinp

                print('Köszönöm')
                break

