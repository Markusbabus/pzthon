import random

üzenetek = ['Biztos',
    'Úgy tűnik',
    'Igen, biztosan',
    'Nincs biztos válaszom',
    'Kérdezd meg újra később',
    'Koncentrálj és kérdezz újra',
    'A válaszom nem',
    'Nem úgy néz ki',
    'Nem']

print(üzenetek[random.randint(0, len(üzenetek) - 1)])