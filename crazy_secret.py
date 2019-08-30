import hashlib
import random

def load_file(filename):
    with open(filename,"rb") as file:
        data = file.read()
        return data

def do_the_hash(data):
    m = hashlib.sha512()
    m.update(data)
    r =  m.hexdigest()
    return r

def main():
    f1 = load_file("file1")
    f2 = load_file("file2")
    h = do_the_hash(f1 + f2)
    for i in range(1000):
        k = h + str(random.random())
        k = k.encode("UTF-8")
        h = do_the_hash(k)
    print(h)

main()
