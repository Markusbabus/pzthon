import matplotlib.pyplot as plt

ca = 1
cb = 1
cc = 0
cd = 0

n_max = 120
k1= 1
k2 = 1.2
dt=0.05
rt = 0
t_sor = [0]
x_grids = [0,]

def dc(k, dt, c1, c2):
    dc1 = float(k * c1 * c2 * dt )
    return dc1


while True:
    print('\033[1mTöbbkomponensű kémia reakció szimuláció\033[0m \n')
    print('A + B → C \nC + B → D\n')
    print('\033[1m(s)\033[0maját vagy az \033[1m(a)\033[0mlap kofigurációk egyikét szeretnéd használni?')
    inp = input()

    if inp == 'a':
        print('\033[1mAlap1\033[0m: \ncₐ = 1 \ncᵦ = 1 \nc𝒸 = 0 \nc𝒹 = 0 \nk₁ = 1 \nk₂ = 1.2 \nΔt = 0.05s \nnmax (lépések száma): 120\n')
        print('\033[1mAlap2\033[0m: \ncₐ = 1 \ncᵦ = 1 \nc𝒸 = 0 \nc𝒹 = 0 \nk₁ = 1.2 \nk₂ = 1 \nΔt = 0.05s \nnmax (lépések száma): 120\n')
        print('\033[1mAlap3\033[0m: \ncₐ = 1 \ncᵦ = 5 \nc𝒸 = 0 \nc𝒹 = 0 \nk₁ = 1.2 \nk₂ = 1 \nΔt = 0.02s \nnmax (lépések száma): 60\n')
        print('\033[1mAlap4\033[0m: \ncₐ = 1 \ncᵦ = 5 \nc𝒸 = 0 \nc𝒹 = 0 \nk₁ = 1.2 \nk₂ = 1 \nΔt = 0.02s \nnmax (lépések száma): 60\n')

        while True:
            print('Írd be a kiválasztott konfiguráció számát!')
            inp = int(input())

            if inp == 1:
                break

            elif inp ==  2:
                k1 = 1.2
                k2 = 1
                break

            elif inp == 3:
                k1 = 1.2
                k2 = 1
                cb = 5
                dt = 0.02
                n_max = 60
                break

            elif inp == 4:
                ca = 2
                cb = 3
                k1 = 1.5
                k2 = 0.5
                break

            else:
                continue

        break

    elif inp == 's':
        while True:
            print('Az A anyag ketdeti koncentrációjának a nagysága (cₐ):')
            ca = float(input())

            if ca < 0:
                continue

            else:
                break

        while True:
            print('A B anyag ketdeti koncentrációjának a nagysága (cᵦ):')
            cb = float(input())

            if cb < 0:
                continue

            else:
                break

        while True:
            print('A C anyag ketdeti koncentrációjának a nagysága (c𝒸):')
            cc = float(input())

            if cc < 0:
                continue

            else:
                break

        while True:
            print('A D anyag ketdeti koncentrációjának a nagysága (c𝒹):')
            cd = float(input())

            if cd < 0:
                continue

            else:
                break

        while True:
            print('A + B Rekciósebességi állandó értéke (k1):')
            k1 = float(input())

            if k1 < 0:
                continue

            else:
                break

        while True:
            print('B + C Rekciósebességi állandó értéke (k2):')
            k2 = float(input())

            if k2 < 0:
                continue

            else:
                break

        while True:
            print('Időlépések nagysága (nem lehet negatív vagy 0):')
            dt = float(input())

            if dt <= 0:
                continue

            elif dt >= 0.15:

                while True:
                    print('Vigyázat: Magasabb értékeknél nem mindig reális lesz az eredmény')
                    print('Biztos ezzel az értékkel szeretnéd folytatni? (y/n)')
                    inp = input()

                    if inp in ('y', 'n'):
                        break

                    else:
                        continue

            if inp == 'n':
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

ca_oszlop = [ca,]
cb_oszlop = [cb,]
cc_oszlop = [cc,]
cd_oszlop = [cd,]

for n in range(n_max):

    dcv1 =  dc(k1, dt, ca, cb)
    dcv2 =  dc(k2, dt, cb, cc)
    ca -= dcv1
    cb -= (dcv1 + dcv2)
    cc += dcv1 - dcv2
    cd += dcv2

    ca_oszlop.append(ca)
    cb_oszlop.append(cb)
    cc_oszlop.append(cc)
    cd_oszlop.append(cd)

    rt += dt
    t_sor.append(round(rt, 3))

print('cₐ = ' + str(ca_oszlop), '\ncᵦ = ' + str(cb_oszlop), '\ncc = ' + str(cc_oszlop), '\ncd = ' + str(cd_oszlop), '\nt = ' + str(t_sor))

fig, ax = plt.subplots()
ax.set(facecolor = '#E0E0E0')
fig.set(facecolor = 'snow')

plt.title('Kétkomponensű kémia reakció szimuláció ', fontsize = 17, weight = 'bold')
plt.xlabel('Eltelt idő (s)', fontsize = 15)
plt.ylabel('c értéke', fontsize = 15)
plt.plot( t_sor, ca_oszlop, color = '#1b9e77', label = 'A anyag koncentrációja')
plt.plot( t_sor, cb_oszlop, color = '#d95f02', label = 'B anyag koncentrációja')
plt.plot( t_sor, cc_oszlop, color = '#7570b3', label = 'C anyag koncentrációja')
plt.plot( t_sor, cd_oszlop, color = '#e7298a', label = 'D anyag koncentrációja')
plt.grid(linestyle = (0, (1, 1)), color ='snow')
plt.legend()
plt.show()