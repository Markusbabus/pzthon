name = ''

while not name :
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
n_of_g = int(input())

if n_of_g:
    print('Be sure to have enough room for all you guests.')

print('Done')