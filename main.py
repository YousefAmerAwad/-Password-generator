import string
import random



lowers = list(string.ascii_lowercase)       #list of lowercase letters that we should randomly choose from
uppers = list(string.ascii_uppercase)       #list of uppercase letters that we should randomly choose from
digits = list(string.digits)                #list of digits that we should randomly choose from
symbols = ['?', '.', ',', '@', '$', '!']    #list of symbols that we should randomly choose from


#To ensure that the user has entered the correct input
n=1
while(n==1):
    try:
        number_of_characters = int(input('Enter the number of characters for the password '))
        n=0
        if (number_of_characters < 6) & (number_of_characters == int(number_of_characters)):
            print('Minimum number of chars is 6')
            n=1

    except ValueError:
        print('Please enter an ineger number')


random.shuffle(lowers)
random.shuffle(uppers)
random.shuffle(digits)
random.shuffle(symbols)

n = int((30/100) * number_of_characters)        
m = number_of_characters - 3 * n

password = lowers[:n] + uppers[:n] + digits[:n] + symbols[:m]
random.shuffle(password)
password = ''.join(password)
print(password)

