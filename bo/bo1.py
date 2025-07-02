import matplotlib.pyplot as plt

t = 0
t_sor = [t]
n1 = 1
n2 = 1
n_oszlop = [n1]
while t < 25:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    t += 1
    n_oszlop.append(n3)
    t_sor.append(t)

print(n_oszlop)

plt.plot(t_sor, n_oszlop)
plt.show()