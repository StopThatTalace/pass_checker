import string
import getpass

def check_password_strength():
    password = getpass.getpass('Enter your password:')
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength <= 1:
        remarks = ('Ouch.. your password isn\'t that strong, change it as soon as possible.')
    elif strength == 2:
        remarks = ('Hmm your password is steal weak, change it as soon as possible.')
    elif strength == 4:
        remarks = ('Okay, why not! But to be honest it can be much better, let\'s make a safer password!')
    elif strength == 8:
        remarks = ('Here\'s a password that can be hard to guess, you are on the right way!')
    elif strength == 16:
        remarks = ('Wow... that\'s a pretty strong password, '
                   'you have something to hide or what?')

    print('So.. your password has:')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{special_count} special characters')
    print(f'Password Score : {strength / 5} out of 5')
    print(f'Remarks: {remarks}')


def check_pwd(another_pw = False):
    valid = False
    if another_pw:
        choice = input('Do you want to check another password ? (y/n) :')
    else:
        choice = input('Do you want to check your password ? (y/n):')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Existing...')
            return False
        else:
            print('Invalid input.. please retry again. \n')


if __name__ == '__main__':
    print('Welcome to Password Strength Checker')