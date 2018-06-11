def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    if user_input.upper() == 'H' or user_input.upper() == 'HELP':
        result = True
    else:
        result = False

    return result


def is_validated_english_sentence(user_input):
    import re

    str_pass = len(re.findall('[a-zA-Z.,?!\s]', user_input))
    str_pass2 = len(re.findall('[.,?!\s]', user_input))
    if len(user_input) == str_pass and str_pass != str_pass2:
        result = True
    else:
        result = False

    return result


def is_validated_morse_code(user_input):
    morse_code = get_morse_code_dict()
    morse_code_val = morse_code.values()
    list_input = user_input.split(' ')
    for i in list_input:
        if i in morse_code_val:
            result = True
        else:
            result = False
            break

    return result


def get_cleaned_english_sentence(raw_english_sentence):
    special_characters = ['.', ',', '?', '!']
    for i in special_characters:
        raw_english_sentence = raw_english_sentence.replace(i, '')

    result = raw_english_sentence.strip()

    return result


def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    morse_code_items = morse_code_dict.items()
    for i, v in morse_code_items:
        if morse_character == v:
            result = i
    return result


def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    morse_code_items = morse_code_dict.items()

    for i, v in morse_code_items:
        if i == english_character.upper():
            result = v

    return result


def decoding_sentence(morse_sentence):
    result = ''
    morse_sentence = morse_sentence.split(' ')
    for i in morse_sentence:
        if not i:
            result += ' '
        else:
            result += decoding_character(i)

    return result


def encoding_sentence(english_sentence):
    english_sentence = get_cleaned_english_sentence(english_sentence)
    english_list = list(english_sentence)
    result = ''

    for morse in english_list:
        if morse == ' ':
            result += ' '
        else:
            morse_code = encoding_character(morse)
            result += morse_code + ' '

    return result.strip()


def main():
    print("Morse Code Program!!")
    while True:
        user_input = input('Input your message(H - Help, 0 - Exit): ')
        if is_help_command(user_input):
            print(get_help_message())
        elif is_validated_english_sentence(user_input):
            print(encoding_sentence(user_input))
        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        elif user_input == '0':
            break
        else:
            print('Wrong Input')
    print("Good Bye")
    print("Morse Code Program Finished!!")


if __name__ == "__main__":
    main()