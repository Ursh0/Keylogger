from Crypto.Cipher import AES  
from secrets import token_bytes
from encryption import decrypt
import re
import sys

# def checkBinFile(filename):
#     pattern = r"\.bin$"
#     return re.search(pattern, filename) is not None

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    # if checkBinFile(filename) is True:
    decrypt(filename)
    # else:
    #     print("Cannot decrypt")


        