import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks

c = 1
c_oszlop = [1,]
n_max = 100
k= 0.69314718
dt=0.05
rt = 0
t_sor = [0]
x_grids = [0,]

while True:
    print('\033[1mEgykomponensű kémia reakció szimuláció\033[0m \n\033[1m(s)\033[0maját vagy az \033[1m(a)\033[0mlap kofigurációt szeretnéd használni?')
    inp = input()

    if inp == 'a':
        break

    elif inp == 's':
        print('Ketdeti koncentráció nagysága:')
        c = float(input())
        c_oszlop = [c, ]

        print('Rekciósebességi állandó értéke:')
        k = float(input())

        while True:
            print('Időlépések nagysága (nem lehet negatív vagy 0):')
            dt = float(input())

            if dt <= 0:
                continue

            else:
                break

        while True:
            print('Időlépések száma (nem lehet negatív vagy 0):')
            n_max = int(input())
            if n_max <= 0:
                continue

            else:
                break

        break

for n in range(n_max):

    c = c + (- k * c * dt)
    c_oszlop.append(c)

    rt += dt
    t_sor.append(round(rt, 3))

    if n % 10 == 0:
        x_grids.append(rt - dt)

x_grids.append(n_max * dt)
print('c = ' + str(c_oszlop), '\nt = ' + str(t_sor))

fig, ax = plt.subplots()
ax.set(facecolor = 'lightgray')
fig.set(facecolor = 'snow')

plt.title('Egykomponensű kémia reakció szimuláció ', fontsize = 17, weight = 'bold')
plt.xlabel('Eltelt idő (s)', fontsize = 15)
plt.ylabel('c értéke', fontsize = 15)
plt.plot( t_sor, c_oszlop, color = 'seagreen')
plt.grid(linestyle = (0, (1, 1)), color ='snow')
if len(x_grids) < 18:
    xticks(x_grids)
plt.show()