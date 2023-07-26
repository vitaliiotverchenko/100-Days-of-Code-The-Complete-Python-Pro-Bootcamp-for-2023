def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            ascii_val = ord(char)
            shifted_ascii = (ascii_val - ord('a') + shift) % 26 + ord('a')
            if is_upper:
                char = chr(shifted_ascii).upper()
            else:
                char = chr(shifted_ascii)
        result += char
    return result


def main():
    logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
    print(logo)
    print('Welcome to the Caesar Cipher!')
    while True:
        action = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if action not in ('encrypt', 'decrypt'):
            print("Invalid input. Please enter 'encrypt' or 'decrypt'.")
            continue

        text = input(f"Enter the text to {action}: ")
        shift = int(input("Enter the shift value (a positive integer): "))

        if action == 'encrypt':
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, -shift)
            print("Decrypted text:", decrypted_text)

        restart = input("Do you want to restart the program? (yes/no): ").lower()
        if restart != "yes":
            print("Goodbye! Exiting the program.")
            break


if __name__ == "__main__":
    main()
