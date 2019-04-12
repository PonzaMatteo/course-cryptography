import argparse
import timeit
import functools
import os
import sys

from Crypto.Hash import *
from Crypto import Random

Random.new()


def main():
    fin, add_salt, repeat_times = parse_args_cli()

    # Init Input string, prepending salt if necessary
    in_bytes = b""
    if add_salt:
        salt = generate_salt()
        in_bytes = salt

    if fin is None:  # Input from CLI
        str_in = input("Insert input string:")
        in_bytes = in_bytes + str_in.encode("utf-8")
    elif os.path.isfile(fin):  # Input from File
        in_bytes = in_bytes + open(fin, "rb").read()
    else:
        print("Error: Input file not exist!")
        sys.exit(-1)

    # Calculate Hash
    if add_salt:
        print("Salt:\t", salt)

    md5 = md5_hash(in_bytes)
    sha1 = sha1_hash(in_bytes)
    sha256 = sha256_hash(in_bytes)

    print("-"*30)
    print("MD5:\t", md5)
    print("SHA1:\t", sha1)
    print("SHA256:\t", sha256)

    # Measure Time
    print("-"*30)
    print(f"Running {repeat_times} times")
    timer_md5 = timeit.Timer(functools.partial(md5_hash, in_bytes))
    md5_time = timer_md5.timeit(repeat_times)
    print("MD5 Time:\t {:.4}s".format(md5_time))

    timer_sha1 = timeit.Timer(functools.partial(sha1_hash, in_bytes))
    sha1_time = timer_sha1.timeit(repeat_times)
    print("SHA1 Time:\t {:.4}s".format(sha1_time))

    timer_sha256 = timeit.Timer(functools.partial(sha256_hash, in_bytes))
    sha256_time = timer_sha256.timeit(repeat_times)
    print("SHA256 Time:\t {:.4}s".format(sha256_time))


def md5_hash(data):
    h = MD5.new(data)
    return h.hexdigest()


def sha1_hash(data):
    h = SHA.new(data)
    return h.hexdigest()


def sha256_hash(data):
    h = SHA256.new(data)
    return h.hexdigest()


def generate_salt(salt_length=8):
    random_salt = Random.get_random_bytes(salt_length)
    return random_salt


def parse_args_cli():
    parser = argparse.ArgumentParser(
        description="Run various hashing method calculating execution time")
    parser.add_argument('--input-file', '-i', action="store", dest="input")
    parser.add_argument('--salt', '-s', action="store_true", dest="salt")
    parser.add_argument("--repeat", "-r", action="store", dest="repeat", type=int, default=100)
    args = parser.parse_args()
    return(args.input, args.salt, args.repeat)


if __name__ == "__main__":
    main()
