hossz = 0
szel = 0
ept = 4
import math

def hosszú():
    global hossz
    while True:

        print('Milyen hosszú a terem? (m)')
        try:
             hossz = float(input())

             if hossz == 0:
                 raise ZeroDivisionError
             break

        except ValueError:
            print('Kérlek számot adj meg!')

        except ZeroDivisionError:
            print('A nulla nem lehetséges.')



def széles():
    global szel
    while True:

        print('Milyen széles a terem? (m)')
        try:
             szel = float(input())

             if szel== 0:
                 raise ZeroDivisionError
             break

        except ValueError:
            print('Kérlek számot adj meg!')

        except ZeroDivisionError:
            print('A nulla nem lehetséges.')

hosszú()
széles()

ter = hossz * szel

print(str(ter) + ' m2 területed van.')

print('Mennyi ember jön?')
emb = input()

if int(emb) * ept > ter :
    print('Nincs elég helyed egy ekkora partira, még ' + str(math.ceil(int(emb) - ter / ept)) + ' embert kell kirúgni')

elif int(emb) * ept <= ter and ter // ept - int(emb) != 0:
    print('Van elég helyed egy ekkora partira, még ' + str(ter // ept - int(emb)) + ' embert hívhatsz meg.')

else:
    print('Pont elegen vagytok.')