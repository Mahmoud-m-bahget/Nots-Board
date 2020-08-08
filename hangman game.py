import random
print('welcome to hang man  game  ')
name = input('what is your fuckn name ? \n')
print('----------------')
print('hello ', name, )
print('try to win the game in less than 10 turns ')

def hangman():
    word = random.choice(['mahmoud', 'mostafa','abdo'])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    gussmade = ''

    while len(word)> 0:
        main = ''
        missed = 0
        for letter in word:
            if letter in gussmade:
                main = main + letter
            else:
                main = main + '_' + ''

        if main in word:
            print(main)
            print('that is my man')
            break
        print('Guess the word ', main)
        guess = input()

        if guess in validletters:
            gussmade = gussmade + guess
        else:
            print('enter a valid character')
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print('9 turns left')
                print('  --------- ')
            elif turns == 8:
                print('8 turns left')
                print('  --------- ')
                print('      O     ')
            elif turns == 7:
                print('7 turns left')
                print('  --------- ')
                print('      O     ')
                print('      |     ')
            elif turns == 6:
                print('6 turns left')
                print('  --------- ')
                print('      O     ')
                print('      |     ')
                print('     /      ')
            elif turns == 5:
                print('5 turns left')
                print('  --------- ')
                print('      O     ')
                print('      |     ')
                print('     / \    ')
            elif turns == 4:
                print('4 turns left')
                print('  --------- ')
                print('    \ O     ')
                print('      |     ')
                print('     / \    ')
            elif turns == 3:
                print('3 turns left')
                print('  --------- ')
                print('    \ O /   ')
                print('      |     ')
                print('     / \    ')
            elif turns == 2:
                print('2 turns left')
                print('  --------- ')
                print('    \ O|/   ')
                print('      |     ')
                print('     / \    ')
            elif turns == 1:
                print('1 turns left')
                print('you are dying')
                print('  --------- ')
                print('    \ O_|/  ')
                print('      |     ')
                print('     / \    ')
            elif turns == 0:
                print('you are dead man')
                print('  --------- ')
                print('      O_|   ')
                print('     /|\    ')
                print('     / \    ')
                break

    return
hangman()
