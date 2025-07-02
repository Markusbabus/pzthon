import sys

while True:
    print('Type exit to exit.')
    resp = input()

    if resp == 'exit' :
        sys.exit()

    print('You typed ' + resp + '.')