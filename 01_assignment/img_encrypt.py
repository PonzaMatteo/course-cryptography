from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

import sys
import os
import argparse

BLOCK_SIZE = 16
Random.new()

def encrypt(str_input, psw):
    key = psw_to_key(psw)
    cipher = AES.new(key)
    str_input = add_pad(str_input)
    str_output = cipher.encrypt(str_input)
    return str_output

def decrypt(str_input, psw):
    key = psw_to_key(psw)
    cipher = AES.new(key)
    str_output = cipher.decrypt(str_input)
    pad_length = str_output[-1] + 1
    return str_output[0 : -pad_length]

def psw_to_key(key):
    h = SHA256.new()
    h.update(key)
    return h.digest()

def add_pad(plaintext):
    pad_length = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
    pad_length = pad_length - 1

    # pad_length <= 16, just one byte is necessary to store it
    random_pad = Random.get_random_bytes(pad_length)
    pad_length_byte = int_to_bytes(pad_length)
    return b''.join([plaintext, random_pad, pad_length_byte])

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def parse_args_cli():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt file with AES256. SHA256 hash of the password is used as encryption key")

    parser.add_argument('--input-file', '-i', action="store", dest="input", default="input.txt")

    parser.add_argument('--output-file', '-o', action="store", dest="output", default="output.txt")

    parser.add_argument('--password', '-psw', action="store", dest="psw", required=True)

    parser.add_argument('--decrypt', '-d', action="store_true", dest="decrypt")

    args = parser.parse_args()
    
    return((args.input, args.output, args.decrypt, args.psw))

def main():
    fin, fout, op_decrypt, psw = parse_args_cli()

    if os.path.isfile(fin):
        input_bytes = open(fin, "rb").read()
        out_bytes = bytes(0)
        psw = psw.encode("utf-8")
        if op_decrypt:
            out_bytes = decrypt(input_bytes, psw)
        else:
            out_bytes = encrypt(input_bytes, psw)
        out_file = open(fout, "wb")
        out_file.write(out_bytes)
    else:
        print("Error: Input file not exist!")
        sys.exit(-1)

if __name__== "__main__":
  main()