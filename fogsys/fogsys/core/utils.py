import hashlib
import random
import datetime

# This function generate 10 character long hash


def create_hash(name):
    random_int = str(random.randint(0, 100))  # generate a random int to compose the hash
    now = str(datetime.datetime.now())  # get the current date time to compose the hash

    concat = ''.join([name, random_int, now])
    return hashlib.sha256(concat.encode('utf-8')).hexdigest()
