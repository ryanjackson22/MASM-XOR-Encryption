# main.py

def xor_encrypt(plain_text: str, key: str):
    # xor_key = 'P'
    cipher_text = ''

    for char in plain_text:
        integer_to_char = chr(ord(char) ^ ord(key))
        cipher_text += integer_to_char

    return cipher_text

def xor_encrypt_key(plain_text: str, key: str):
    cipher_text = ''

    for index in range(len(plain_text)):
        integer_to_char = chr(ord(plain_text[index]) ^ ord(key[index]))
        cipher_text += integer_to_char

    return cipher_text

def main():
    pass

if __name__ == "__main__":
   main()