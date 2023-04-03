import random

print('H A N G M A N  # 8 attempts')
amount_win = []
amount_lose = []
while True:
    game_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    while game_choice not in ['play', 'results', 'exit']:
        game_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if game_choice == 'exit':
        exit()
    elif game_choice == 'results':
        print('You won:', len(amount_win), 'times')
        print('You lost:', len(amount_lose), 'times')
        continue
    elif game_choice == 'play':
        pass
    word = random.choice(['python', 'java', 'swift', 'javascript'])
    num, length = 8, len(word)
    enc_word = list(len(word)*'-')
    while num != 0:
        print(''.join(enc_word))
        given_input = input('Input a letter: ')
        if len(given_input) > 1 or given_input in ("", " "):
            print("Please, input a single letter.")
            continue
        elif given_input not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please, enter a lowercase letter from the English alphabet.')
            continue
        if given_input in word and given_input not in enc_word and given_input in 'abcdefghijklmnopqrstuvwxyz':
            for number in range(len(word)):
                if word[number] == given_input:
                    enc_word[number] = given_input
                    if '-' not in enc_word:
                        num = 0
                        print('You guessed the word '+''.join(enc_word)+'!\nYou survived!')
                        amount_win.append(1)
        elif given_input in enc_word and given_input in 'abcdefghijklmnopqrstuvwxyz':
            print("You've already guessed this letter.")
            continue
        else:
            num = num - 1
            print("That letter doesn't appear in the word.\n")
            if num == 0:
                print('\nYou lost!')
                amount_lose.append(1)


