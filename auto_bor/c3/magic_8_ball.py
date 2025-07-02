import random

def get_ans(ansnumb):

    if ansnumb == 1 :
        return 'Ez biztos'

    if ansnumb == 2 :
        return 'Határozottan így van'

    if ansnumb == 3 :
        return 'Igen'

    if ansnumb == 4 :
        return 'A válasz homályos, kérdezz újra'

    if ansnumb == 5 :
        return 'Kérdezz később'

    if ansnumb == 6 :
        return 'Koncentrálj és kérdezz újra'

    if ansnumb == 7 :
        return 'A válaszom nem'

    if ansnumb == 8 :
        return 'Nem túl jók a kilátások'

    if ansnumb == 9 :
        return 'Nagyon kétséges'

print(get_ans(random.randint(1,9)))