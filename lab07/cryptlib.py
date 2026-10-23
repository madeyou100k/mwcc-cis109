# LAB 07: Encryption Library

# Function to encrypt a message by shifting letters.
def encrypt(message, shift):

    # Store the encrypted message.
    result = ""

    # Loop through each character in the message.
    for char in message:

        # Check if the character is an uppercase letter.
        if "A" <= char <= "Z":

            # Find the letter's position in the alphabet.
            position = ord(char) - ord("A")

            # Shift the letter and wrap around the alphabet.
            new_position = (position + shift) % 26

            # Convert the position back into an uppercase letter.
            result += chr(new_position + ord("A"))

        # Check if the character is a lowercase letter.
        elif "a" <= char <= "z":

            # Find the letter's position in the alphabet.
            position = ord(char) - ord("a")

            # Shift the letter and wrap around the alphabet.
            new_position = (position + shift) % 26

            # Convert the position back into a lowercase letter.
            result += chr(new_position + ord("a"))

        else:
            result += char

    # Return the encrypted message.
    return result

# Function to decrypt a message.
def decrypt(message, shift):

    # Reverse the shift to restore the original message.
    return encrypt(message, -shift)
