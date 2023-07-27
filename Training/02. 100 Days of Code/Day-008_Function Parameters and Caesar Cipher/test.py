# Exercise 3: Caesar Cipher Part 1 - Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']

# prompt input user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(alphabet.index("b"))


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

                    # encode char by position + shift
                    encode_text += alphabet[pos + shift]

        # check if there is space
        else:
            encode_text += " "

    # print the encode text
    return print(f"Here's the encoded result: {encode_text}!")


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
                    pos = idx

                    # decode text by position - shift
                    decode_text += alphabet[pos - shift]

        # check if there is space
        else:
            decode_text += " "

    # print the decode text
    return print(f"Here's the decoded result: {decode_text}!")


print(len(alphabet))
