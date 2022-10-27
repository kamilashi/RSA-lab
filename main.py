import math
import random


def power(x, y, p):  # returns (x^y) % p
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p;
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;


def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4);
    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True;
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;


def isPrime(testValue, accuracy):
    # Corner cases
    if (testValue <= 1 or testValue == 4):
        return False;
    if (testValue <= 3):
        return True;

    d = testValue - 1;
    while d % 2 == 0:
        d //= 2;

    for i in range(accuracy):
        if (miillerTest(d, testValue) == False):
            return False;
    return True;


def getPrimeOfLength(bits):
    trialOfLength = pow(2, bits - 1);  # the first even number of the given bit length for testing
    while True:
        while True:
            increment = random.randrange(1, 9);  # find an odd increment
            if increment % 2 != 0:
                break
        trialOfLength += increment;
        if isPrime(trialOfLength, 4):
            break
        print(str(trialOfLength) + " is not prime. searching further...");
    return trialOfLength;


def getCoPrimeTo(number):
    e = 65537;
    while (math.gcd(e, number) != 1):
        e += 2;
    return (e);


length = 4;
p = getPrimeOfLength(length);
print("p = " + str(p));
q = getPrimeOfLength(length);
while(p==q):
    q = getPrimeOfLength(length);
print("q = " + str(q));

n = p * q;
phi = (p - 1) * (q - 1);

print("phi  = = (p - 1) * (q - 1) = " + str(phi));

e = getCoPrimeTo(phi);
print("e = " + str(e));

#numOfPrimes = math.trunc(x / math.trunc(math.log(x)));





# qustions: does e need to have the same bit length as p and q?
