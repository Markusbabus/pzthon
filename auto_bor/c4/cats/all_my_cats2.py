pet_names = []

while True:
    print('Írd be házi állat ' + str(len(pet_names) +1) + ' nevét (vagy semmit, hogy vége legyen):')
    name = input()

    if name == '':
        break

    pet_names = pet_names + [name]

print('A házi állatok nevei:')

for name in pet_names:
    print(' ' + name)