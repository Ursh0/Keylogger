from Crypto.Cipher import AES  
from secrets import token_bytes
from encryption import decrypt
import re
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    decrypt(filename)


        
        