import math
import sys
import random
from egcd import egcd


def power(x, y, p):  # returns (x^y) % p
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)

    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False


def isPrime(testValue, accuracy):
    # Corner cases
    if (testValue <= 1 or testValue == 4):
        return False
    if (testValue <= 3):
        return True

    d = testValue - 1
    while d % 2 == 0:
        d //= 2

    for i in range(accuracy):
        if (miillerTest(d, testValue) == False):
            return False
    return True


def getPrimeOfLength(bits):
    # the first even number of the given bit length for testing
    trialOfLength = pow(2, bits - 1)
    while True:
        while True:
            increment = random.randrange(1, 9)  # find an odd increment
            if increment % 2 != 0:
                break
        trialOfLength += increment
        if isPrime(trialOfLength, 4):
            break
        #print(str(trialOfLength) + " is not prime. searching further...");
    return trialOfLength


def getCoPrimeTo(number):
    e_candidate = 65537
    while (math.gcd(e_candidate, number) != 1):
        e_candidate += 2
    return (e_candidate)


length = 2048
# for debugging:
#p = 7;
#q = 11;
#e = 17;

p = getPrimeOfLength(length)
print("p = " + str(p))

q = getPrimeOfLength(length)
while (p == q):
    q = getPrimeOfLength(length)
print("q = " + str(q))

n = p * q  # public key 1
phi = (p - 1) * (q - 1)

print("n  =  " + str(n))

e = getCoPrimeTo(phi)
print("e = " + str(e))  # public key 2
[gcd, d, u] = egcd(e, phi)
if (d < 0):
    d = d % phi
print("d = " + str(d))  # private key

# numOfPrimes = math.trunc(x / math.trunc(math.log(x)));


m = 1234567
# print("initial m = " + str(m));


def squareAndMultiply(x, k, n):
    k = reverseBits(k)
    res = 1
    while (k > 0):
        if (k & 1 == 0):
            res = (res * res) % n
            res * x  # fake multiplication
        else:
            res = (res * res * x) % n
        k = k >> 1
    return res


def reverseBits(number):
    bit_size = sys.getsizeof(number)
    string = "{:" + str(bit_size) + "b}"
    reversed = int(string.format(number)[::-1], 2)
    return reversed


# encipher:
c = squareAndMultiply(m, e, n)
# print("c = " + str(c));

# decipher:
deciphered_m = squareAndMultiply(c, d, n)
# print("m = " + str(deciphered_m));
