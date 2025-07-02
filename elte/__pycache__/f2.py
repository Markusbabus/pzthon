import matplotlib.pyplot as plt

y_szám = 0
c = 1
c_oszlop = [1,]
n_sor = [0,]
y_grids = []

for n in range(100):
    c += 2
    c_oszlop.append(c)
    n_sor.append(n + 1)

for i in range(10):
    y_szám += 20
    y_grids.append(y_szám)

print('c = ' + str(c_oszlop), '\nn = ' + str(n_sor))

ax = plt.axes()
ax.set(facecolor = 'lightgray')

plt.title('c értékének növelése 2-vel', fontsize = 20, weight = 'bold')
plt.xlabel('Növelések száma', fontsize = 15)
plt.ylabel('c értéke', fontsize = 15)
plt.plot( n_sor, c_oszlop,)

plt.grid()
plt.yticks(y_grids)
plt.show()