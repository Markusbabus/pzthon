
def count_l(lista):
    elsők = ''
    utolsó = ''
    if len(lista) == 0:
        return ''

    elif len(lista) == 1:
        return lista[0]

    else:

        for i in range(len(lista)):
            if i != len(lista)-1:
                elsők += lista[i] + ', '

            if i == len(lista)-1:
                utolsó = 'and ' + lista[i]

        return elsők + utolsó

spam = [111]

print(count_l(spam))