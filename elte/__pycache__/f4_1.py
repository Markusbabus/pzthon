import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks

cb, cb1 = 2, 2
ca, ca1 = 1, 1
ca_oszlop = [ca,]
cb_oszlop = [cb,]
n_max = 100
k= 0.69314718
dt=0.05
rt = 0
t_sor = [0]
x_grids = [0,]
vt = 0
vt_oszlop = [vt, ]


while True:
    print('\033[1mKétkomponensű kémia reakció szimuláció\033[0m \n\033[1m(s)\033[0maját vagy az \033[1m(a)\033[0mlap kofigurációt szeretnéd használni?')
    inp = input()

    if inp == 'a':
        break

    elif inp == 's':
        print('Az első komponens ketdeti koncentrációjának a nagysága (cₐ):')
        ca = ca1= float(input())
        ca_oszlop = [ca, ]

        print('A második komponens ketdeti koncentrációjának a nagysága (cᵦ):')
        cb = cb1= float(input())
        cb_oszlop = [cb, ]

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

    ca += (- k * ca * cb * dt)
    cb += (- k * ca * cb * dt)
    ca_oszlop.append(ca)
    cb_oszlop.append(cb)

    vt = ca1 - ca
    vt_oszlop.append(vt)

    rt += dt
    t_sor.append(round(rt, 3))

    if n % 10 == 0:
        x_grids.append(rt - dt)

x_grids.append(n_max * dt)
print('cₐ = ' + str(ca_oszlop), '\ncᵦ = ' + str(cb_oszlop), '\nvt = ' + str(vt_oszlop), '\nt = ' + str(t_sor))

fig, ax = plt.subplots()
ax.set(facecolor = 'lightgray')
fig.set(facecolor = 'snow')

plt.title('Kétkomponensű kémia reakció szimuláció ', fontsize = 17, weight = 'bold')
plt.xlabel('Eltelt idő (s)', fontsize = 15)
plt.ylabel('c értéke', fontsize = 15)
plt.plot( t_sor, ca_oszlop, color = '#0072B8', label = 'Reagens 1')
plt.plot( t_sor, cb_oszlop, color = '#FF6F20', label = 'Reagens 2')
plt.plot( t_sor, vt_oszlop, color = '#FFD700', label = 'Végtermék')
plt.grid(linestyle = (0, (1, 1)), color ='snow')
plt.legend()
if len(x_grids) < 18:
    xticks(x_grids)
plt.show()