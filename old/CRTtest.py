import json
import math
import sys
import random

import numpy
from egcd import egcd
m = 43;
# # encipher:
# d = 53;
# p = 7;
# q = 11;
# e = 17;
# n = p * q;  # public key 1s
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

path = "./keys/public/pub.json"
with open(path, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

e = json_object['e'];
print("public key e = " + str(e));


[gcd, v, u] = egcd(q, p);
print("v = " + str(v));
print("u = " + str(u));
d_p = d % (p - 1);
d_q = d % (q - 1);
print("d_p = " + str(d_p));
print("d_q = " + str(d_q));

sig_p = pow((m % p), d_p, p);
sig_q = pow((m % q), d_q, q);
# sig_p = squareAndMultiply((m % p), d_p, n) % p;
# sig_q = squareAndMultiply((m % q), d_q, n) % q;

print("sig_p = " + str(sig_p));
print("sig_q = " + str(sig_q));
sig1 = u * p * sig_q;
sig2 = v * q * sig_p;

sig = sig1 + sig2;
if(sig<0):
    sig = sig % (p*q)
print("signed character = " + str(sig));

deciphered_m = squareAndMultiply(sig, e, n);
print("m = " + str(deciphered_m));
