import random

titkn = random.randint(1, 20)

print('Gondoltam egy számra 1 és 20 között.')

for próbák in range (1, 7):
    print('Tippelj!')
    tipp = int(input())

    if tipp < titkn:
        print('Túl kicsit tippeltél.')

    elif tipp > titkn:
        print('Túl nagyot tippeltél.')

    else:
        break

if tipp == titkn:
    print('Ügyes vagy! Eltaláltad a számot ' + str(próbák) + ' próba alatt!')

else:
    print('Nem találtad el. A szám ' + str(titkn) + ' volt.')