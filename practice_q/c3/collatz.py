import sys


def collatz():
    while True:
        print('A számod:')
        numb = input()


        try :numb = int(numb)

        except ValueError:
            print('Kérlek számot adj meg')
            continue

        if  numb < 1:

            print('Kérlek nullánál nagyobb számot adj meg')

        else:
            break

    while numb != 1:
        if numb % 2 == 0:
            numb = numb // 2
            print(numb)

        elif numb % 2 ==1:
            numb = numb * 3 + 1
            print(numb)





collatz()