def multiplication(user_input):
    result = []
    for i in range(1,10):
        answer = i * user_input
        result.append(answer)

    return result


def print_result(user_input):
    for i in range(1,10):
        answer = i * int(user_input)
        print('{0} X {1} = {2}'.format(user_input, i, answer))


def is_digit(user_input):
    try:
        if 0 < int(user_input) < 10:
            result = True
        else:
            result = False
    except:
        result = False

    return result

def main():
    print('welcome to the multiplication table')
    while True:
        user_input = input('Which table do you want to know(1~9, Exit - 0): ')
        if is_digit(user_input):
            print(print_result(user_input))
        elif user_input == '0':
            break
        else:
            print('Wrong input, input again.')
    print('Thank you for using this program')


if __name__ == '__main__':
    main()