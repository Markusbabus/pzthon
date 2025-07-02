hossz = 0
szel = 0
ept = 4
import math

while not hossz :
    print('Milyen hosszú a terem? (m)')
    hossz = input()

while not szel:
    print('Milyen széles a terem? (m)')
    szel = input()

ter = int(hossz) * int(szel)

print(str(ter) + ' m2 területed van.')

print('Mennyi ember jön?')
emb = input()

if int(emb) * ept > ter :
    print('Nincs elég helyed egy ekkora partira, még ' + str(math.ceil(int(emb) - ter / ept)) + ' embert kell kirúgni')

if int(emb) * ept <= ter and ter // ept - int(emb) != 0:
    print('Van elég helyed egy ekkora partira, még ' + str(ter // ept - int(emb)) + ' embert hívhatsz meg.')

else:
    print('Pont elegen vagytok.')