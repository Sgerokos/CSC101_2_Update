# Import the hashlib package into Python
import hashlib

# Import the sys package into Python
import sys
# Print the list of guaranteed hashing algorithms
print(hashlib.algorithms_guaranteed)

# Ask the user to choose an encryption method from the list or get help
hash = input("Please choose an encryption method.\n" 
             "Please enter one of the following:\n" 
             "sha3_384, blake2s, shake_256, md5-sha1," 
             "whirlpool, sm3, shake_128,"  
             "sha384, sha512, sha3_512," 
             "\nripemd160, md5, blake2b, sha3_256," 
             "sha512_224, md4, sha256, sha512_256, sha3_224, sha224, sha1,\n" 
             "mdc2, or help for assistance in choosing: ")

# If help is entered, list the algorithms and what they are
if hash == "help":
    print("\nSHA stands for Secure Hash Algorithm.\n"
          "\nSHA1, SHA2, and SHA3 are all different algorithms.\n"
          "\nSHA1 has one hash function and is similar to MD4 and MD5.\n"
          "SHA1 is 20 bytes long.\n"
          "\nSHA2 has five hash functions:\n"
          "SHA-224 is 28 bytes,\n" 
          "SHA-256 is 32 bytes,\n"
          "SHA-384 is 48 bytes,\n" 
          "SHA-512/224 is 28 bytes,\n" 
          "SHA-512/256 is 32 bytes.\n"  
          "\nSHA3 is similar to SHA2. SHA3 includes:\n"
          "sha3_224, sha3_256, sha3_384, sha3_512.\n"
          "\nshake is part of SHA3. Shake includes:\n" 
          "shake_128 is 128 bytes,\n" 
          "shake_256 is 256 bytes.\n"
          "\nBlake2 is a strong encryption which is as fast as md5 and more secure.\n"
          "Blake2b is 64 bytes long. Blake2s is 8-32 bytes long.\n"
          "\nRipemd160 is similar to SHA1 and is 20 bytes long.\n"
          "\nSM3 is a strong algorithm offering a 256-bit encryption.\n"
          "\nMDC2 is 128 bytes long.\n"
          "\nMD4 and MD5 are two of the oldest and weakest hashes.\n"
          "MD4 and MD5 produce a 128-bit message.\n"
          "\nFor security, choose any besides ripemd160, mdc2, md4, or md5.\n"
          "For better encryption from the SHA family, choose any sha2 or sha3.\n")

    # Ask the user to input the encryption method again if help was chosen
    hash = input("Now please choose an encryption method.\n" 
                 "Please enter one of the following:\n" 
                 "sha3_384, blake2s, shake_256, md5-sha1," 
                 "whirlpool, sm3, shake_128,"  
                 "sha384, sha512, sha3_512," 
                 "\nripemd160, md5, blake2b, sha3_256," "sha512_224, md4, sha256, sha512_256, sha3_224, sha224, sha1: ")

#Get the user's message to encrypt
message = input("Please enter the message you would like to encrypt: ").encode('utf-8')

#Use the chosen hashing algorithm to encrypt the user's message
if hash in hashlib.algorithms_guaranteed:
    h = hashlib.new(hash)
    h.update(message)
    print("The encrypted message using", hash, "is:")
    print(h.hexdigest())
else:
    print("Invalid choice of encryption method.")