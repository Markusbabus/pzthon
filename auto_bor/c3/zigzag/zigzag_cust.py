import time, sys
indent = 0
indent_inc = True
idő = 0
szél = 0
szél_ki = 0



while True:
    print('Milyen széles testet akarsz?')
    szél = input()

    try:
        szél = int(szél)

        if szél == 0:
            print('A szám nem lehet nulla!')

        else:
            break

    except ValueError:
        print('Kérlek számot adj meg!')

while True:
    print('Mennyire szélesen akarod hogy mozogjon?')
    szél_ki = input()

    try:
        szél_ki = int(szél_ki)

        if szél_ki == 0:
            print('A szám nem lehet nulla!')

        else:
            break

    except ValueError:
        print('Kérlek számot adj meg!')

while True :
    print('Mennyi szünetet akarsz a részek közt?(s)')
    idő = input()

    try:
        idő = float(idő)

        if idő == 0:
            print('A szám nem lehet nulla!')

        else:
            break

    except ValueError:
        print('Kérlek számot adj meg!')


try:
    while True:
        print(' ' * indent, end='')
        print('*' * szél)
        time.sleep(idő)

        if indent_inc:
            indent = indent + 1

            if indent == szél_ki:
                indent_inc = False

        else:
            indent = indent - 1
            if indent == 0:
                indent_inc = True

except KeyboardInterrupt:
    sys.exit()