import random 

correct = random.randint(1000,9999)
print('The correct answer is:', correct)
cow = 0
bulls = 0
count = 0
guess = int(input('Enter your guess '))

while guess != correct:
    if guess != correct: 
        for index in range (0, 4):
            guess = str(guess)
            correct = str(correct)
            if guess[index] == correct[index]:
                cow = cow + 1
                # print(cow)
            if guess[index] in correct and not guess[index] == correct[index]:
                bulls = bulls + 1
        count = count + 1 
        print('You have made', count, 'guess(es)')
    if guess == correct:
        print('You guessed correctly')
        break
        

    print('number of cows is ', cow)
    print('number of bulls', bulls)
    print('\nGuess again')
    guess = int(input('Enter your guess '))
    cow = 0
    bull = 0

