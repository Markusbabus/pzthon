t = 0
p = ''

while not p:
    print('Meddig akarunk számokat összeadni?')
    p = input()

p = int(p) + 1

for n in range(p):
    t = t + n

print(t)