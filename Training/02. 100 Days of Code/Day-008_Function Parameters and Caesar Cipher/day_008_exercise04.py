# Exercise 4: Caesar Cipher Part 3 - Reorganising our code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v',
            'w', 'x', 'y', 'z']


# Combine function encode and decode, shift, and direction into caesar function
def caesar(start_text, num_shift, choice_direction):
    # define final text as a blank string
    final_text = ""

    # do loop to check each letter in start_text
    for letter in start_text:

        # check if letter in alphabet
        if letter in alphabet:

            # get index of letter of start_text in alphabet
            pos = alphabet.index(letter)

            # if choice direction = encode
            if choice_direction == "encode":

                # new_pos = pos + num_shift
                new_pos = pos + num_shift

                # if new pos is larger than len of alphabet
                if new_pos > len(alphabet):

                    # check the remain
                    remain = new_pos - len(alphabet) + 1

                    # add into final_text
                    final_text += alphabet[remain]

                else:
                    # if new_pos < len(alphabet), then add directly the letter into final_text
                    final_text += alphabet[new_pos]

            elif choice_direction == "decode":

                # new_pos = pos - num_shift
                new_pos = pos - num_shift

                # check if new_pos < 0
                if new_pos < 0:

                    # check the remain
                    remain = new_pos - 1

                    # add into final_text
                    final_text += alphabet[remain]

                else:
                    # if new pos > 0, add the letter into final_text
                    final_text += alphabet[new_pos]

        else:
            # check if there is space, add directly to final_text
            final_text += letter

    # print out the final_text
    return print(f"Final Text of {choice_direction} is {final_text} !")


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
        caesar(text, shift, "encode")

    elif direction == "decode":
        caesar(text, shift, "decode")

    # ask if you want to play again
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "yes":
        play_on = True
    else:
        play_on = False
