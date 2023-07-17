print ('Wow! You are welcome to this cool game')
answer = input('Do you want to play? (yes/no)')

score = 0
total_questions = 4

if answer.lower() == 'yes':
    answer = input('1. What is the coolest Coding Language?')

    if answer.lower() == 'python':
        score += 1
        print('Correct')

    else: 
        print('Incorrent')

    answer = input('2. Do you think  I am on Twitter?')
    if answer.lower() == 'yes':
        score += 1
        print('Correct')
    else:
        print('Incorrect : (')
    
    answer = input('3. Do you think I am on Youtube?')

    if answer.lower() == 'Yes':

        score += 1
        print('Right')

    else: 
        print ('Wrong')

print('Thanks for being part of this awesome game')

mark = (score/total_questions)*100
print('Mark Obtained:', mark)
print('Bye!')