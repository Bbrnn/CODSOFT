import random
import string


#Use the string module to get the required characters
lower = string.ascii_lowercase

upper = string.ascii_uppercase

digits = string.digits

symbols = string.punctuation

#concatenate all the characters
all_characters = lower + upper + digits + symbols

length= int(input("The desired length of your password:\n"))

if length >= 12 and length <= len(all_characters):

    # Ensure the password contains at least one lowercase letter, one uppercase letter, one digit, and one symbol
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    
    #Generate the remaining password
    password += random.sample(all_characters, length - 4)

    #Convert the password to a list and shuffle it
    password = list(password)
    random.shuffle(password)

    #Join the list to from the final password
    password = ''.join(password)
    print("Generated password is:", password)

else:
    print("Invalid length of password.Please enter a number bewteen 12", len(all_characters))