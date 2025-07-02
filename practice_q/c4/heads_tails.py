import random
numberOfStreaks = 0
flip = []

for n in range(10000):
    if random.randint(0, 1) ==1:
            flip.append(1)

    else:
            flip.append(0)

    for i in range(len(flip) -5):
        if flip[i] == flip[i + 1] == flip[i + 2] == flip[i + 3] == flip[i + 4] == flip[i + 5]:
                numberOfStreaks += 1


    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 1000000))