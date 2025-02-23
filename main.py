# main.py

def xor_encrypt(plain_text: str, key: str):
    # xor_key = 'P'
    cipher_text = ''

    for char in plain_text:
        integer_to_char = chr(ord(char) ^ ord(key))
        cipher_text += integer_to_char

    return cipher_text

def main():
    pass

if __name__ == "__main__":
   main()