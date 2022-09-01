'''
Number Guessing game<

This is one of the simple python projects yet an exciting one. You
can even call it a mini-game. Make a program in which the
computer randomly chooses a number between 1 to 10, 1 to 100, or
any range. Then give users a hint to guess the number. Every time
the user guesses wrong, he gets another clue, and his score gets
reduced. The clue can be multiples, divisible, greater or smaller, or a
combination of all
'''
import random


def guess():
    # computer_guess = 3
    computer_guess = random.choice(range(100))
    life = 5
    hint = []
    if computer_guess % 2 == 0 :
        hint.append('The number is an even number')
    if computer_guess % 2 == 1 :
        hint.append('The number is an odd number')
    while life != 0:
        try:
            user = int(input('Enter number : '))
            if user > computer_guess :
                if 'The number is less than your guess' not in hint :                    
                    hint.append('The number is less than your guess')
                if 'The number is greater than your guess'  in hint :
                    hint.remove('The number is greater than your guess')
            if user < computer_guess :
                if 'The number is greater than your guess' not in hint :
                    hint.append('The number is greater than your guess')
                if 'The number is less than your guess' in hint :                    
                    hint.remove('The number is less than your guess')
            if user == computer_guess :
                print('Congratulations your guess is correct ')
                return
            game_hint = ''.join(f'{val}\n' for val in hint)
            print('Your guess is not correct')
            print("***"*10)
            print(game_hint) 
            life -= 1
            print(f'Your life remain {life}')
        except ValueError :
            print('Enter a digit number')
            life -= 1
            print(f'Your life remain {life}')
    print('Game over ')



if __name__ == "__main__" :
    guess()