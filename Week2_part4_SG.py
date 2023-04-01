# imports the hashlib package into python
import hashlib

# Imports the sys package into python
import sys

def print_algorithm_list():
    """Prints a list of available hash algorithms."""
    print("""
Please choose an encryption method.
Please enter one of the following:

sha3_384, blake2s, shake_256,
shake_128, sha384, sha512, sha3_512,
md5, blake2b, sha3_256,
sha256, sha3_224, sha224, sha1,
or type "help" for assistance in choosing.
""")


def print_algorithm_descriptions():
    """Prints descriptions of available hash algorithms."""
    print("""
SHA stands for Secure Hash Algorithm.

SHA1, SHA2, and SHA3 are all three different algorithms.

sha1 has one hash function and is similar to MD5.
sha1 is 10 bytes long.

sha2 has two hash functions available: 
SHA-224 is 28 bytes, SHA-256 is 32 bytes, 
SHA-384 is 48 bytes.

SHA3 is similar to SHA2: sha3_384, sha384, sha3_512,
sha3_224 is 28 bytes, sha3_256 is 32 bytes. 
These are all SHA3 algorithms.

shake is part of SHA3: shake_128 is 128 bytes, 
shake_256 is 256 bytes.

blake2 is a strong encryption which is as fast as md5 and more secure.
blake2b is 64 bits long, blake2s is 8-32 bytes long.

MD5 is one of the oldest and weakest hashes.
MD5 produces a 128 bit message.

For security, choose any besides sha1 and md5.
For better encryption from the SHA family, choose any sha2 or sha3.
""")


def get_hash_algorithm():
    """Asks the user to choose a hash algorithm, and returns the chosen algorithm."""
    while True:
        print_algorithm_list()
        hash_choice = input().strip().lower()

        if hash_choice == "help":
            print_algorithm_descriptions()
        elif hash_choice in hashlib.algorithms_guaranteed:
            return hash_choice
        else:
            print(f"{hash_choice} is not a valid hash algorithm. Please try again.")


def get_hashed_message(hash_choice, message):
    """Hashes the given message using the given hash algorithm, and returns the hashed message."""
    hasher = getattr(hashlib, hash_choice)
    return hasher(message.encode()).hexdigest()


def main():
    hash_choice = get_hash_algorithm()
    message = input("What would you like to encrypt? Please enter it now: ")
    hashed_message = get_hashed_message(hash_choice, message)
    print(f"The {hash_choice} hash of {message} is:\n{hashed_message}")


if __name__ == "__main__":
    main()