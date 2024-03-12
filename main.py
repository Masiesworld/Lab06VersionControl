'''Encode part: Macy Yu'''
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode \n2. Decode \n3. Quit\n')


def encoder(string):
    res = []
    for i in string:
        res.append(str(int(i) + 3))
    res = ''.join(res)
    return res


def main():
    while True:
        print_menu()
        user_choice = int(input('Please enter an option: '))
        if user_choice == 1:
            user_string = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')

        elif user_choice == 2:
            encoded_string = encoder(user_string)
            print(f'The encoded password is {encoded_string}, and the original password is {user_string}.')

        elif user_choice == 3:
            break

if __name__ == '__main__':
    main()