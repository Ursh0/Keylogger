from Crypto.Cipher import AES  
from secrets import token_bytes
import re
import os
import sys
import logging

# logging.basicConfig(filename="debug.log", level=logging.DEBUG)

key = token_bytes(16)

# log_file = "logs.txt"
clipBoard_file = "clipBoardLogs.txt"

def resource_path(relative_path):
    """ Get the absolute path to the resource, adjusting for PyInstaller's executable environment. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

key_file_path = resource_path("encryption_key.bin")

def encryptContents(file):

    with open(file, "r") as file:
        try:
            contents = file.read()
            cipher = AES.new(load_key(), AES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(contents.encode('ascii'))
            return createEncryptedFile(nonce, ciphertext, tag, file.name)
        except Exception as e:
            logging.error(f"Failed to encrypt: {e}")

def createEncryptedFile(nonce, ciphertext, tag, fileName):
    fileName = createBinFile(fileName)
    with open(fileName, "wb") as efile:
        efile.write(nonce)          
        efile.write(tag)            
        efile.write(ciphertext)
    return fileName   


def createBinFile(fileName):
    match = re.search(r"^.*?(?=\.)", fileName)
    if match:
        filename = match.group() + ".bin"
        return filename
    print("ok")
    return None


def save_key():
    if not os.path.exists(key_file_path):
        key = token_bytes(16)
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
        print("Encryption key saved.")
    else:
        print("Encryption key already exists.")

def load_key():
    with open(key_file_path, "rb") as key_file:
        return key_file.read()

def decrypt(eFile):
    with open(eFile, "rb") as file:
        nonce = file.read(16)          
        tag = file.read(16)            
        ciphertext = file.read()   
        cipher = AES.new(load_key(), AES.MODE_EAX, nonce=nonce)
    
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        decryptedText = plaintext.decode('ascii') 
        with open("decryptedFile", "w") as decryptedFile:
            decryptedFile.write(decryptedText)

    except ValueError:
        print("Key incorrect or message corrupted")
        return None



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python encryption.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    encryptContents(filename)