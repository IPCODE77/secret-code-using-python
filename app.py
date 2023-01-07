import time
import string
import random


work = 'Welcome to morsh code convertion lets start 😎 '
for i in range(len(work)):
    time.sleep(0.1)
    print(work[i], end='')

print('\n')
user = input(
    'Enter What Do You Want Enter code for \'C\' and Decoding for \'D\': ')


def code():
    # pass
    user_input = input('Enter Word: ')
    if len(user_input) <= 2:
        newvalue = "".join(reversed(user_input))
        print(f'Your secrect word is {newvalue}')
    else:
        bigword = user_input[0]
        splitword = user_input[1:len(user_input)]
        splitword += bigword
        first_char = ''
        last_char = ''
        for i in range(3):
            first_char += random.choice(string.ascii_letters)
            last_char += random.choice(string.ascii_letters)
        print(f' your secrect word is :-- {first_char}{splitword}{last_char}')
        # print(splitword)


def decode():
    user_input = input('Enter Word to decode: ')
    if len(user_input) <= 2:
        newvalue = "".join(reversed(user_input))
        print(f'Your Decode word is {newvalue}')
    else:
        decodeword = []
        startvalue = ''
        finalvalue = ""
        # string convert to list
        for i in range(len(user_input)):
            decodeword.append(user_input[i])
        for i in range(0, 3):
            del decodeword[0]
            del decodeword[-1]
        # for i in range(0,3):
        startvalue = decodeword.pop(-1)
        for i in range(len(decodeword)):
            finalvalue += decodeword[i]
        print(f'Your decode word is {startvalue}{finalvalue}')


if user == 'C':
    code()
elif user == 'D':
    decode()
