import random, time, copy

WIDTH = 60
HEIGHT = 40

# Listák listája a sejtekhez
next_cells = []

for x in range(WIDTH):
    column = []  # új oszlop

    for y in range(HEIGHT):

        if random.randint(0, 1) == 0:
            column.append('#')  # élő sejt hozzáadása

        else:
            column.append(' ')  # halott sejt

    next_cells.append(column)  # next_cells az oszlop listák listája

while True:  # a fő loop
    print('\n\n\n\n\n')  # a lépések elválasztása newlines-al
    current_cells = copy.deepcopy(next_cells)

    # current_cells kinyomtatása
    for y in range(HEIGHT):

        for x in range(WIDTH):
             print(current_cells[x][y], end=' ')  # # vagy space nyomtatása

        print()  # newline nyomtatása a sor végén

    # következő lépés kiszámítása a jelenlegi szerint
    for x in range(WIDTH):

        for y in range(HEIGHT):
            # a szomszédos kordináták megszerzése
            # '% WIDTH' miatt a left_coord mindig -1 és 0 között lesz
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # az élő szomszédok megszámlálása
            num_neighbors = 0

            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1  # a balfelső életben van

            if current_cells[x][above_coord] == '#':
                num_neighbors += 1  # a felső életben van

            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1  # a jobbfelső életben van

            if current_cells[left_coord][y] == '#':
                num_neighbors += 1  # a bal életben van

            if current_cells[right_coord][y] == '#':
                num_neighbors += 1  # a jobb életben van

            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1  # a balalsó életben van

            if current_cells[x][below_coord] == '#':
                num_neighbors += 1  # az alsó életben van

            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1  # a jobbalsó életben van

            # a sejtek megadássa conway alapján
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                # élő sejtek 1 v 2 szomszéddal túlélik
                next_cells[x][y] = '#'

            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                # hallot sejtek 3 szomszéddal életre kelnek
                next_cells[x][y] = '#'

            else:
                # minden más halott lesz
                next_cells[x][y] = ' '
    time.sleep(1)