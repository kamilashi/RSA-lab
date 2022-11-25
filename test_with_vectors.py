import sys
import json
from egcd import egcd
import decode_text
import encode_text

inputs = ["vector 1", "Vector 2", "Vector 3"];
outputs = [];


# @params: encode_text.main(vectorTest, input)
# boolean vectorTest - True: pass input as the second parameter from this script
#                    - False: use the plaintext/m.txt as input, pass whatever as the second parameter
# input: the plain text to decipher

# @params: decode_text.main(vectorTest, input, CRTon)
# boolean vectorTest - True: pass input as the second parameter from this script
#                    - False: use the plaintext/m.txt as input, pass whatever as the second parameter
# input: the plain text to decipher
# boolean CRTon - True: compute using the Chinese Remainder Theorem
#               - False: compute using the Square and Multiply algorithm



for input in inputs:
    encodedMessage = encode_text.main(True, input);
    decodedMessage = decode_text.main(True, encodedMessage, False);
    outputs.append(decodedMessage);

print("Initial test vector: ");
print(inputs);

print("Deciphered output: ");
print(outputs);