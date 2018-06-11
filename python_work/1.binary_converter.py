# 십진수 - 이진수 변환 프로그램
# Without any modules including numpy

def input_b(user_input):
    if user_input.upper() == 'B':
        result = True
    else:
        result = False

    return result


def input_d(user_input):
    if user_input.upper() == 'D':
        result = True
    else:
        result = False

    return result


def binary_to_decimal(binary_input):
    result = 0
    if int(binary_input) >= 0:
        for i in range(len(binary_input)):
            result += int(binary_input[0]) * (2 ** i)
    else:
        binary_input = str(int(binary_input) * -1)
        for i in range(len(binary_input)):
            result += int(binary_input[0]) * (2 ** i)
        result = result * -1

    return result


def decimal_to_binary(decimal_input):
    result = ''
    decimal_input = int(decimal_input)

    if decimal_input > 0:
        while decimal_input != 0:
            remainder = decimal_input % 2
            decimal_input = decimal_input // 2
            result = str(remainder) + result
    elif decimal_input == 0:
        result = 0

    else:
        decimal_input = decimal_input * -1
        while decimal_input != 0:
            remainder = decimal_input % 2
            decimal_input = decimal_input // 2
            result = str(remainder) + result
        result = '-' + result

    return result


def is_decimal_value(decimal_input):
    try:
        decimal_input = int(decimal_input)
        if decimal_input != 0 or decimal_input != -0:
            result = True
        else:
            result = False
    except:
        result = False

    return result


def is_binary_value(binary_input):
    binary_set = {'0', '1'}
    user_set = set()

    #Make it able to have a negative number
    if binary_input[0] == '-':
        binary_input = binary_input[1:]

    for i in binary_input:
        user_set.add(i)

    if not binary_input:
        result = False
    elif binary_input == '0' or binary_input == '-0':
        result = False
    elif len(binary_set.union(user_set)) == 2:
        result = True
    else:
        result = False

    return result


def main():
    print('Welcome to binary - decimal converter!')
    continue_program = 1

    while continue_program:
        user_input = input('Type "B" for binary -> decimal, "D" for decimal ->binary(0 - Exit): ')

        # Converting binary to decimal
        if input_b(user_input):
            while True:
                binary_input = input('Input binary number: ')
                if is_binary_value(binary_input):
                    print(binary_to_decimal(binary_input))
                    break
                elif binary_input == '0':
                    continue_program = 0
                    break
                else:
                    print('Wrong input, Input again')

        # Converting decimal to binary
        elif input_d(user_input):
            while True:
                decimal_input = input('Input decimal number: ')
                if is_decimal_value(decimal_input):
                    print(decimal_to_binary(decimal_input))
                    break
                elif decimal_input == '0':
                    continue_program = 0
                    break
                else:
                    print('Wrong input, Input again')

        # Finish program
        elif user_input == '0':
            break

        else: print('Wrong input, Input again')

    print('Thank you for using this program!')


if __name__ == '__main__':
    main()


