def xor_encrypt(plain_text):
    xor_key = 'P'
    cipher_text = ''

    for char in plain_text:
        integer_to_char = chr(ord(char) ^ ord(xor_key))
        cipher_text += integer_to_char

    return cipher_text


def main():
    sample_string = "Max Carney"

    encrypted_string = xor_encrypt(sample_string)
    print("Decrypted String:", encrypted_string)

    decrypted_string = xor_encrypt(encrypted_string)
    print("Decrypted String:", decrypted_string)

if __name__ == "__main__":
   main()