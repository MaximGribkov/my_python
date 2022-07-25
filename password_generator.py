import random

print('Select "1" for lowercase, uppercase and numbers\n' 
      'Select "2" for lowercase, uppercase, numbers and special characters (!, @, #, $, %, ^, &, *, ?, ~)')
len_password = int(input('Length password '))
enter_mode = input('Enter mode ')

lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
             'm', 'n', 'b', 'v', 'c', 'x', 'z', 'l', 'k', 'j']
uppercase = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
             'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'L', 'K', 'J']
numbers = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
special_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '~']


def generator_password(*args):
    new_password = []
    if enter_mode == '1':
        all_list = lowercase + uppercase + numbers
        for i in range(0, len_password + 1):
            new_password.append(random.choice(all_list))
            password = ' '.join(new_password)
        print(password.replace(' ', ''))
    if enter_mode == '2':
        all_list = lowercase + uppercase + numbers + special_symbols
        for i in range(0, len_password + 1):
            new_password.append(random.choice(all_list))
            password = ' '.join(new_password)
        print(password.replace(' ', ''))


if __name__ == '__main__':
    generator_password(len_password, enter_mode)