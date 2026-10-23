# LAB 07: Caesar Cipher Command-Line Utility
# CIS109 - Python Programming
# This program encrypts or decrypts messages using the Caesar cipher.

# Import argparse for command-line arguments.
import argparse

# Import encryption and decryption functions.
from cryptlib import encrypt, decrypt


# Main function for the program.
def main():

    # Create the argument parser.
    parser = argparse.ArgumentParser(
        description="Caesar Cipher Encryption Utility"
    )

    # Prevent the user from selecting encrypt and decrypt together.
    group = parser.add_mutually_exclusive_group(required=True)

    # Option to encrypt a message.
    group.add_argument(
        "-e",
        action="store_true",
        help="Encrypt the message"
    )

    # Option to decrypt a message.
    group.add_argument(
        "-d",
        action="store_true",
        help="Decrypt the message"
    )

    # Accept the message entered by the user.
    parser.add_argument(
        "-m",
        required=True,
        help="Message to encrypt or decrypt"
    )

    # Allow the user to choose the shift amount.
    parser.add_argument(
        "-s",
        type=int,
        default=3,
        help="Number of positions to shift (default: 3)"
    )

    # Read the command-line arguments.
    args = parser.parse_args()

    # Encrypt the message if -e was selected.
    if args.e:
        result = encrypt(args.m, args.s)
        print(result)

    # Decrypt the message if -d was selected.
    elif args.d:
        result = decrypt(args.m, args.s)
        print(result)


# Run the main function when the script is executed.
if __name__ == "__main__":
    main()
