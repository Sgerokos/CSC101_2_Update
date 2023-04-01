# imports the hashlib package into Python
import hashlib

# Imports the sys package into Python
import sys

# List of available hash algorithms with descriptions
hashes = {
    "md5": "MD5 (128-bit)",
    "sha1": "SHA-1 (160-bit)",
    "sha224": "SHA-224 (224-bit)",
    "sha256": "SHA-256 (256-bit)",
    "sha384": "SHA-384 (384-bit)",
    "sha512": "SHA-512 (512-bit)",
    "sha3_224": "SHA-3 (224-bit)",
    "sha3_256": "SHA-3 (256-bit)",
    "sha3_384": "SHA-3 (384-bit)",
    "sha3_512": "SHA-3 (512-bit)",
    "blake2b": "BLAKE2 (up to 64-byte output)",
    "blake2s": "BLAKE2 (up to 32-byte output)",
    "md4": "MD4 (128-bit)",
    "mdc2": "MDC-2 (128-bit)",
    "ripemd160": "RIPEMD-160 (160-bit)",
    "sm3": "SM3 (256-bit)",
    "shake_128": "SHA-3 (extendable output) with 128-bit output",
    "shake_256": "SHA-3 (extendable output) with 256-bit output"
}

# Prompt the user to choose a hash algorithm
while True:
    hash = input("Please choose a hash algorithm:\n{}\n".format("\n".join(hashes.keys())))
    if hash in hashes:
        break
    else:
        print("Invalid choice. Please choose a valid hash algorithm.")

# Prompt the user to enter a message to be encrypted
while True:
    message = input("Please enter the message to be encrypted:\n")
    if message:
        break
    else:
        print("Invalid input. Please enter a non-empty message.")

# Encrypt the message using the chosen hash algorithm
hash_object = hashlib.new(hash)
hash_object.update(message.encode())
digest = hash_object.hexdigest()

# Print the encrypted message
print("The {} hash of the message is:\n{}".format(hashes[hash], digest))