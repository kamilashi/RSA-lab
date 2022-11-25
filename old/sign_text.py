import sys
import json
from egcd import egcd


# Opening JSON file
path = "./keys/private/priv.json"
with open(path, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

d = json_object['d'];
print("private key d = " + str(d));
n = json_object['n'];
print("private key n = " + str(n));
q = json_object['q'];
p = json_object['p'];

path = "./plaintext/m.txt"
plaintext = [];
with open(path) as f:
    for line in f:
        for char in line:
            plaintext.append(char);

print("signing:  " + str(plaintext));


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


def CRT(m, u, v, d_p, d_q, p, q):
    sig_p = pow((m % p), d_p, p);
    sig_q = pow((m % q), d_q, q);
    # print("sig_p = " + str(sig_p));
    # print("sig_q = " + str(sig_q));
    sig1 = u * p * sig_q ;
    sig2 = v * q * sig_p;
    # print("sig1 = " + str(sig1));
    # print("sig2 = " + str(sig2));
    sig = sig1 + sig2;
    if (sig < 0):
        sig = sig % (p * q)
    return sig;


signaturetext = "";
# encipher:
# d = 53;
# p = 7;
# q = 11;
# e = 17;
# n = p * q;  # public key 1s

# choosing method:
withCRT = False;
if (withCRT == False):
    print("CRT off ");
    for charInt in plaintext:
        sig = squareAndMultiply(ord(charInt), d, n);
        signaturetext += str(sig) + "\n";
        print("enciphered character = " + str(sig));
else:
    print("CRT on ");
    [gcd, v, u] = egcd(q, p);
    print("v = " + str(v));
    print("u = " + str(u));
    d_p = d % (p - 1);
    d_q = d % (q - 1);
    print("d_p = " + str(d_p));
    print("d_q = " + str(d_q));
    for charInt in plaintext:
        sig = CRT(ord(charInt), u, v, d_p, d_q, p, q);
        signaturetext += str(sig) + "\n";
        print("signed character = " + str(sig));

# write to file:
path = "./signaturetext/sig.txt"
with open(path, 'w+') as f:
    f.write(str(signaturetext));
