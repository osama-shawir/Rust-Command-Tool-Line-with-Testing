import argparse

# Define the Caesar cipher encryption function
def encrypt_caesar(plaintext, shift):
    result = []
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            shifted = char
        result.append(shifted)
    return ''.join(result)

# Define the Caesar cipher decryption function
def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def main():
    parser = argparse.ArgumentParser(description='Caesar Cipher CLI')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the message')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the message')
    parser.add_argument('--message', type=str, required=True, help='The message to encrypt or decrypt')
    parser.add_argument('--shift', type=int, default=3, help='The shift value for the Caesar cipher')
    parser.add_argument('--uppercase', action='store_true', help='Output in uppercase')

    args = parser.parse_args()

    if args.encrypt:
        result = encrypt_caesar(args.message, args.shift)
    elif args.decrypt:
        result = decrypt_caesar(args.message, args.shift)
    else:
        print('Please specify either --encrypt or --decrypt')
        return

    if args.uppercase:
        result = result.upper()

    print(result)

if __name__ == '__main__':
    main()


import argparse
import time

# Define the Caesar cipher encryption function
def encrypt_caesar(plaintext, shift):
    result = []
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            shifted = char
        result.append(shifted)
    return ''.join(result)


# Define the Caesar cipher decryption function
def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def main():
    start_time = time.time()  # Record the start time
    parser = argparse.ArgumentParser(description='Caesar Cipher CLI')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the message')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the message')
    parser.add_argument('--message', type=str, required=True, help='The message to encrypt or decrypt')
    parser.add_argument('--shift', type=int, default=3, help='The shift value for the Caesar cipher')
    parser.add_argument('--uppercase', action='store_true', help='Output in uppercase')

    args = parser.parse_args()

    if args.encrypt:
        result = encrypt_caesar(args.message, args.shift)
    elif args.decrypt:
        result = decrypt_caesar(args.message, args.shift)
    else:
        print('Please specify either --encrypt or --decrypt')
        return

    if args.uppercase:
        result = result.upper()

    print(result)

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1_000_000  # Convert to microseconds
    print(f'Execution Time: {execution_time:.6f} microseconds')

if __name__ == '__main__':
    main()
