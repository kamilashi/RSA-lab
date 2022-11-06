import sys
import json

# Opening JSON file
path = "./keys/public/pub.json"
with open(path, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

e = json_object['e'];
print("public key e = " + str(e));
n = json_object['n'];
print("public key n = " + str(n));

path = "./plaintext/m.txt"
with open(path) as f:
    lines = f.readlines()
m = int(lines[0]);
print("read m as = " + str(m));


def squareAndMultiply(x, k, n):
    k = reverseBits(k);
    res = 1;
    while (k > 0):
        if (k & 1 == 0):
            res = (res * res) % n;
            res * x  # fake multiplication
        else:
            res = (res * res * x) % n;
        k = k >> 1
    return res;


def reverseBits(number):
    bit_size = sys.getsizeof(number);
    string = "{:" + str(bit_size) + "b}";
    reversed = int(string.format(number)[::-1], 2);
    return reversed


# encipher:
c = squareAndMultiply(m, e, n);
print("c = " + str(c));

#write to file:

path = "./ciphertext/c.txt"
with open(path, 'w+') as f:
    f.write(str(c));