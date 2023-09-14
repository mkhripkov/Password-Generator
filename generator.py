import secrets # Using secrets to generate the password rather than random is more secure

possible_characters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*()?'

password_length = int(input('How long would you like your password to be?'))

password = ''

for x in range(password_length):
    password += secrets.choice(possible_characters) # secrets randomly selects a character and adds it to the password string
    
print(f'Your password is: {password}')