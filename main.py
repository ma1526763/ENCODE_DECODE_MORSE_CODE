# MORSE CODE DICTIONARY
def morse_code():
    MORSE_CODE_DICT = {
        'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•',
        'F': '••-•', 'G': '--•', 'H': '••••', 'I': '••', 'J': '•---',
        'K': '-•-', 'L': '•-••', 'M': '--', 'N': '-•', 'O': '---',
        'P': '•--•', 'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-',
        'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-', 'Y': '-•--',
        'Z': '--••', '1': '•----', '2': '••---', '3': '•••--', '4': '••••-',
        '5': '•••••', '6': '-••••', '7': '--•••', '8': '---••', '9': '----•',
        '0': '-----', ', ': '--••--', '•': '•-•-•-', '?': '••--••',
        '/': '-••-•', '-': '-••••-', '(': '-•--•', ')': '-•--•-', " ": '/'
    }
    return MORSE_CODE_DICT

# GET INPUT FROM USER
def get_text_input(morse_key_list):
    text = input("Please enter your text to be converted into morse code: ").upper()
    while not text:
        print("Morse code can't be empty.", end="")
        text = input("Please enter your text to be converted into morse code: ").upper()
    for character in text:
        if character in morse_key_list:
            continue
        else:
            print("Invalid character found.Morse code contains all the letters of the English alphabet, numbers from 0 to 9\nand some common punctuation marks like '.' , ',' , '?'\n")
            get_text_input(morse_key_list)
    return text

# ENCODING MORSE CODE
def encode_morse(text_to_convert, morse_dict):
    return "".join([morse_dict[character] + " " for character in text_to_convert])

# DECODING MORSE CODE
def decode_morse(morse_string, morse_dict):
    inverse_morse_dictionary = {v: k for k, v in morse_dict.items()}  # INVERSE MORSE_DICTIONARY
    return "".join([inverse_morse_dictionary[morse_char] for morse_char in morse_string.split(" ") if morse_char])

morse_dictionary = morse_code()
text_input = get_text_input(list(morse_dictionary.keys()))
text_to_morse = encode_morse(text_input, morse_dictionary)
print(text_to_morse)
decode_message = decode_morse(text_to_morse, morse_dictionary)
print(decode_message)
