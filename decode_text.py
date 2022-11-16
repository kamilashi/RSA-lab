import sys
import json

# Opening JSON file
path = "./keys/private/priv.json"
with open(path, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

d = json_object['d'];
print("private key d = " + str(d));
n = json_object['n'];
print("private key n = " + str(n));

path = "./ciphertext/c.txt"
ciphertext = [];
with open(path) as f:
    for line in f:
            ciphertext.append(line);
print("ciphertext = " + str(ciphertext));


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
    reversedInt = int(string.format(number)[::-1], 2);
    return reversedInt


plaintext = "";
# decipher:
for charInt in ciphertext:
    c = squareAndMultiply(int(charInt), d, n);
    plaintext += chr(c);
    print("desiphered character = " + chr(c));

#write to file:

path = "./plaintext/m.txt"
with open(path, 'w+') as f:
    f.write(str(plaintext));