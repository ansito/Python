# Exercise 3: Caesar Cipher Part 1 - Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']


# function encode
def encode(input_text, shift_number):
    # define encode text
    encode_text = ""

    # do loop for check each letter on text
    for letter in input_text:

        # check if letter is in the alphabet
        if letter in alphabet:
            # get to know the position of the letter in alphabet list
            pos = alphabet.index(letter)

            # do + shift_number for encode
            new_pos = pos + shift_number

            # check if new pos is > len of alphabet
            if new_pos > len(alphabet):

                # check the remain, it should be + 1 because index position needs to be +1 if compare with len
                remain = new_pos - len(alphabet) + 1

                # add the new letter into encode_text based on remain position of alphabet
                encode_text += alphabet[remain]

            else:
                # add the new letter into encode_text
                encode_text += alphabet[new_pos]

        # else if letter is space, then add directly to the encode_text
        else:
            encode_text += letter

    return print(f"Here's the encoded result: {encode_text} !")


# function decode

def decode(input_encode_text, shift_number):
    # define decode text
    decode_text = ""

    # do loop to check each letter on input encode text
    for letter in input_encode_text:

        # if letter is in the alphabet
        if letter in alphabet:

            # get to know the position of the letter in alphabet list
            pos = alphabet.index(letter)

            # do - shift for decode
            new_pos = pos - shift_number

            # check if new_pos < 0
            if new_pos < 0:

                # check the remain, it should be - 1, because alphabet[-1] start with "z"
                remain = new_pos - 1

                # add the new letter into decoded_text based on remain position on alphabet
                decode_text += alphabet[remain]

            else:
                # add the new letter into decoded_text
                decode_text += alphabet[new_pos]

        # else if there is space that not in the alphabet
        else:
            decode_text += letter

    return print(f"Here's the decoded result: {decode_text} !")


# main program
# define variable play on
play_on = True

# do while loop
while play_on:

    # prompt input user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # if the direction is encoded
    if direction == "encode":
        encode(text, shift)

    elif direction == "decode":
        decode(text, shift)

    # ask if you want to play again
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "yes":
        play_on = True
    else:
        play_on = False
