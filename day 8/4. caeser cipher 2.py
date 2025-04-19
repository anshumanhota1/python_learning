alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.



# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


# def decrypt(original_text , shift_amount):

#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# decrypt(original_text=text, shift_amount=shift)


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


# encrypt(original_text=text, shift_amount=shift)


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def caesar(original_text , shift_amount, encrypt_or_decrypt):

#     cipher_text = ""
#     for letter in original_text:

#         if encrypt_or_decrypt == "decode":

#             shift_amount *= -1

#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the {encrypt_or_decrypt}d result: {cipher_text}")


# caesar(original_text=text, shift_amount=shift, encrypt_or_decrypt=direction)


def caesar(original_text, shift_amount, encrypt_or_decrypt):
    cipher_text = ""
    # If decoding, reverse the shift
    if encrypt_or_decrypt == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position + shift_amount) % 26
            cipher_text += alphabet[shifted_position]
        else:
            # If it's not a letter (e.g., space or punctuation), just add it unchanged
            cipher_text += letter

    print(f"Here is the {encrypt_or_decrypt}d result: {cipher_text}")

caesar(original_text=text, shift_amount=shift, encrypt_or_decrypt=direction)