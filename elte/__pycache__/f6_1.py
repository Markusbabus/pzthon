import matplotlib.pyplot as plt
import numpy as np


def dc1(c_tömb, p_tömb):
    dcv1 = p_tömb[2] * np.power(c_tömb[0], p_tömb[4]) * c_tömb[1] * p_tömb[1]
    return dcv1


def dc2(c_tömb, p_tömb):
    dcv2 = p_tömb[3] * np.power(c_tömb[0], p_tömb[5]) * np.power(c_tömb[2], p_tömb[6]) * np.power(c_tömb[3], p_tömb[7]) * p_tömb[1]
    return dcv2


c_tömb = np.array([10, 2, 0, 0, 0, 0], dtype=np.float64)         #ca, cb, cc, cd, ce, cf
p_tömb = np.array([500, 0.0005, 1, 1, 2, 2, 2, 2])                     #nmax, dt, k1, k2, x1, x2, y, z


ca_oszlop = np.zeros(int(p_tömb[0]) + 1)
cb_oszlop = np.zeros(int(p_tömb[0]) + 1)
cc_oszlop = np.zeros(int(p_tömb[0]) + 1)
cd_oszlop = np.zeros(int(p_tömb[0]) + 1)
ce_oszlop = np.zeros(int(p_tömb[0]) + 1)
cf_oszlop = np.zeros(int(p_tömb[0]) + 1)
t_sor = np.zeros(int(p_tömb[0]) + 1)

ca_oszlop[0] = c_tömb[0]
cb_oszlop[0] = c_tömb[1]
cc_oszlop[0] = c_tömb[2]
cd_oszlop[0] = c_tömb[3]
ce_oszlop[0] = c_tömb[4]
cf_oszlop[0] = c_tömb[5]

for n in range(1, int(p_tömb[0]) + 1):
    temp_dc1 = dc1(c_tömb, p_tömb)
    temp_dc2 = dc2(c_tömb, p_tömb)
    c_tömb[0] += - temp_dc1 - temp_dc2
    c_tömb[1] += - temp_dc1 + temp_dc2
    c_tömb[2] += 2 * temp_dc1 - temp_dc2
    c_tömb[3] += 2 * temp_dc1 - temp_dc2
    c_tömb[4] += 4 * temp_dc1 + 6 * temp_dc2
    c_tömb[5] += 5 * temp_dc2

    ca_oszlop[n] = c_tömb[0]
    cb_oszlop[n] = c_tömb[1]
    cc_oszlop[n] = c_tömb[2]
    cd_oszlop[n] = c_tömb[3]
    ce_oszlop[n] = c_tömb[4]
    cf_oszlop[n] = c_tömb[5]

    t_sor[n] = t_sor[n - 1] + p_tömb[1]

c_matrix = np.array([ca_oszlop, cb_oszlop, cc_oszlop, cd_oszlop, ce_oszlop, cf_oszlop])

hossz = len(c_matrix[0])
print('cₐ = ' + str(c_matrix[0, 0:hossz:10]),
      '\ncᵦ = ' + str(c_matrix[1, 0:hossz:10]),
      '\ncc = ' + str(c_matrix[2, 0:hossz:10]),
      '\ncd = ' + str(c_matrix[3, 0:hossz:10]),
      '\nce = ' + str(c_matrix[4, 0:hossz:10]),
      '\ncf = ' + str(c_matrix[5, 0:hossz:10]),
      '\nt = ' + str(t_sor[0:hossz:10]))

fig, ax = plt.subplots()
ax.set(facecolor='#E0E0E0')
fig.set(facecolor='snow')

plt.title('Kétkomponensű kémia reakció szimuláció ', fontsize=17, weight='bold')
plt.xlabel('Eltelt idő (s)', fontsize=15)
plt.ylabel('c értéke', fontsize=15)

szín = np.array(['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#beaed4', '#ffff99'])
név = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
átt = 0.7

for i in range(0, len(c_matrix)):

    if c_tömb[2] == c_tömb[3] and név[i] == 'D':
        plt.plot(t_sor, c_matrix[i], color=szín[i], label=név[i] + ' anyag koncentrációja', alpha=átt)

    elif név[i] in ('E', 'F'):
        plt.plot(t_sor, c_matrix[i], color=szín[i], label=név[i] + ' anyag koncentrációja', alpha=átt)

    else:
        plt.plot(t_sor, c_matrix[i], color=szín[i], label=név[i] + ' anyag koncentrációja')

plt.ylim(-0.5, np.max(c_matrix[0: 3] + 1))

plt.grid(linestyle=(0, (1, 1)), color='snow')
plt.legend()
plt.show()
