import random


def get_random_number():
    result = random.randrange(100,1000)
    return result


# Help function for is_validated_number
def is_three_digit_int(user_input_number):
    try:
        if 100 <= int(user_input_number) < 1000:
            result = True
        else:
            result = False
    except:
        result = False

    return result


# Help function for is_validated_number
def is_duplicated_number(three_digit):
    user_input = set()
    for i in three_digit:
        user_input.add(int(i))

    if len(user_input) == 3:
        result = True
    else:
        result = False

    return result


def is_validated_number(user_input_number):
    if is_three_digit_int(user_input_number) and is_duplicated_number(user_input_number):
        result = True
    else:
        result = False

    return result


# Get a random number that fits for this game
def get_not_duplicated_random():
    while True:
        random_set = set()
        random_int = get_random_number()

        for i in str(random_int):
            random_set.add(i)

        if len(random_set) == 3:
            break

    result = random_int

    return result


# Return list with int type
def get_strikes_or_ball(user_input_number, random_number):
    strikes = 0
    user_set = set(user_input_number)
    random_set = set(str(random_number))

    for i, j in zip(user_input_number, random_number):
        if i == j:
            strikes += 1
            user_set.remove(i)
    balls = len(user_set.intersection(random_set))

    result = [strikes, balls]

    return result


def is_yes(one_more_input):
    if one_more_input.upper() == 'Y' or one_more_input.upper() == 'YES':
        result = True
    else:
        result = False

    return result


def is_no(one_more_input):
    if one_more_input.upper() == 'N' or one_more_input.upper() == 'NO':
        result = True
    else:
        result = False

    return result


def main():
    print("Play Baseball")
    play_game = 1
    random_number = str(get_not_duplicated_random())

    while play_game:
        print("Random Number is : ", random_number)
        user_input = input('Input guess number: ')

        # Input the right number to start the game
        if is_validated_number(user_input):
            strikes_balls = get_strikes_or_ball(user_input, random_number)
            print('Strikes: {0}, Balls: {1}'.format(strikes_balls[0], strikes_balls[1]))

            # Got the answer
            if strikes_balls[0] == 3:
                while True:
                    input_yn = input('You win, one more(Y/N)? ')
                    if is_yes(input_yn):
                        random_number = str(get_not_duplicated_random())
                        break
                    elif is_no(input_yn):
                        play_game = 0
                        break
                    else:
                        print('Wrong input, Input again')

        elif user_input == '0':
            break
        else:
            print('Wrong input, Input again')

    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
