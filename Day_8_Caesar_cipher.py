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
