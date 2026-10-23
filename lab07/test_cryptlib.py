# LAB 07: Encryption Library

from cryptlib import encrypt, decrypt

# Check if letters shift forward by 3.
def test_encrypt():
    assert encrypt("ABC", 3) == "DEF"

# Check if encrypted letters can be decrypted.
def test_decrypt():
    assert decrypt("DEF", 3) == "ABC"

# Check if letters wrap around the alphabet.
def test_wraparound():
    assert encrypt("XYZ", 3) == "ABC"

# Check if lowercase letters stay lowercase.
def test_lowercase():
    assert encrypt("abc", 2) == "cde"

# Check if spaces, numbers, and punctuation stay the same.
def test_preserve_spaces_and_numbers():
    assert encrypt("Hello World 123!", 3) == "Khoor Zruog 123!"

# Check if decryption restores the original message.
def test_decrypt_restores_original():
    message = "Hello World!"
    encrypted = encrypt(message, 5)
    assert decrypt(encrypted, 5) == message
