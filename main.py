# Birthday Program
birth_year = input('What year were you born? ')
age = 2022 - int(birth_year)
print(f'Your age is: {age}')

#Password Checker Program
username = input('What is your username? ')
password = input('What is your password? ')
password_length = len(password)
masked_password = '*' * password_length

print(f'{username}, your password {masked_password} is ({password_length}) letters long')
