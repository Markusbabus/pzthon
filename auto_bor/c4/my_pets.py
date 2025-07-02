my_pets = ['Feluka', 'Remzi', 'Tiffany', 'Kaien', 'Iceman', 'Marcellusz', 'Manka', 'Sansa']
print('Írd be az egyik állatom nevét:')
name = input()

if name not in my_pets:
    print('Nincs ' + name + ' nevű állatom')

else:
    print(name + ' a(z) ' + str(my_pets.index(name) + 1) + ' állatom')