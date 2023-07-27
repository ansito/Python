# Exercise 3: Caesar Cipher Part 1 - Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']


# function encode
def encode(input_text):
    # define encode text
    encode_text = ""

    # do loop for check each letter on text
    for letter in input_text:

        # check if letter is in alphabet
        if letter in alphabet:
            for idx, char in enumerate(alphabet):
                if char == letter:
                    # get position of char
                    pos = idx

                    # check if pos + shift is more than len of the alphabet, it means it reached the max len of alphabet
                    # the remainder continue from the start of alphabet
                    if pos + shift > len(alphabet):

                        # calculate the remain
                        remain = (pos + shift) - len(alphabet)

                        # encode char by position + remain + 1, because index = len - 1, so it need to plus 1
                        encode_text += alphabet[remain + 1]

                    else:
                        # encode char by position + shift
                        encode_text += alphabet[pos + shift]

        # check if there is space
        else:
            encode_text += " "

    # print the encode text
    return print(f"Here's the encoded result: {encode_text}!")


# function decode

def decode(input_encode_text):
    # define decode text
    decode_text = ""

    # do loop to check each letter on input encode text
    for letter in input_encode_text:

        # check if input encode text is in alphabet
        if letter in alphabet:
            # do loop in alphabet list to check one by one the list with letter on input encode text
            # get the position of char and do decode
            for idx, char in enumerate(alphabet):
                if char == letter:
                    # get position of char
                    pos = idx

                    # check if pos - shift is less than 0, then make remainder for continuing
                    if pos - shift < 0:

                        # calculate the remain
                        remain = pos - shift

                        # decode text by using remain - 1
                        decode_text += alphabet[remain - 1]

                    else:
                        # decode text by position - shift
                        decode_text += alphabet[pos - shift]

        # check if there is space
        else:
            decode_text += " "

    # print the decode text
    return print(f"Here's the decoded result: {decode_text}!")


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
        encode(text)

    elif direction == "decode":
        decode(text)

    # ask if you want to play again
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "yes":
        play_on = True
    else:
        play_on = False
