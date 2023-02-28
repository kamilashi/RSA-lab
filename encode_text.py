import sys
import json
import time


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
    reversedInt = int(string.format(number)[::-1], 2)
    return reversedInt


def main(vectorTest=False, input=0):
    startTimeEncodeWithoutCRT = time.time()
    # Opening JSON file
    path = "./keys/public/pub.json"
    with open(path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    e = json_object['e']
    # print("public key e = " + str(e));
    n = json_object['n']
    # print("public key n = " + str(n));

    plaintext = []

    if (vectorTest == False):
        path = "./plaintext/m.txt"
        with open(path) as f:
            for line in f:
                for char in line:
                    plaintext.append(char)
    else:
        plaintext = list(input)
    # print("enciphering:  " + str(plaintext));

    ciphertext = ""
    # encipher:
    for charInt in plaintext:
        c = squareAndMultiply(ord(charInt), e, n)
        
        ciphertext += str(c) + "\n"

        # print("enciphered character = " + str(c));

    #encodeTimeWithoutCRT = []
    #endTimeEncodeWithoutCRT = time.time()
    #elapsedTimeWithoutCRT = endTimeEncodeWithoutCRT - startTimeEncodeWithoutCRT
    #encodeTimeWithoutCRT.append(elapsedTimeWithoutCRT)
    # write to file:
    path = "./ciphertext/c.txt"
    # path_to_test = "./ciphertext/c_to_test.txt"
    # with open(path_to_test, 'w+') as fc:
    #     fc.write("")
    #     fc.write(str(c_to_test))

    with open(path, 'w+') as f:
        f.write("")
        f.write(str(ciphertext))
    return ciphertext


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
