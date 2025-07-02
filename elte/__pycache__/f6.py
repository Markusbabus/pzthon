import matplotlib.pyplot as plt
import numpy as np

ca = 10
cb = 2
cc = 0
cd = 0
ce = 0
cf = 0

n_max = 500
dt = 0.0005
k1 = 1
k2 = 1
x1 = 2
x2 = 2
y = 2
z = 2

c_tömb = np.array([ca, cb, cc, cd, ce, cf], dtype=np.float64)
p_tömb = np.array([n_max, dt, k1, k2, x1, x2, y, z])

def dc1(c_tömb, p_tömb):
    dcv1 = p_tömb[2] * np.power(c_tömb[0], p_tömb[4]) * c_tömb[1] * p_tömb[1]
    return dcv1

def dc2(c_tömb, p_tömb):
    dcv2 = p_tömb[3] * np.power(c_tömb[0], p_tömb[5]) * np.power(c_tömb[2], p_tömb[6]) * np.power(c_tömb[3], p_tömb[7]) *  p_tömb[1]
    return dcv2

ca_oszlop = np.zeros(n_max + 1)
cb_oszlop = np.zeros(n_max + 1)
cc_oszlop = np.zeros(n_max + 1)
cd_oszlop = np.zeros(n_max + 1)
ce_oszlop = np.zeros(n_max + 1)
cf_oszlop = np.zeros(n_max + 1)
t_sor = np.zeros(n_max + 1)

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
plt.plot( t_sor, cd_oszlop, color = '#e7298a', label = 'D anyag koncentrációja', alpha = 0.7)
plt.plot( t_sor, ce_oszlop, color = '#beaed4', label = 'E anyag koncentrációja', alpha = 0.7)
plt.plot( t_sor, cf_oszlop, color = '#ffff99', label = 'F anyag koncentrációja', alpha = 0.7)

plt.ylim(0, 11)

plt.grid(linestyle = (0, (1, 1)), color ='snow')
plt.legend()
plt.show()