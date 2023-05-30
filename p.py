import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'
length = 8
filename = 'password.txt'

with open(filename, 'w') as file:
    for combination in itertools.product(alphabet, repeat=length):
        string = ''.join(combination)
        file.write(string + '\n')
