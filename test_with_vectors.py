
import decode_text
import encode_text
import sign_text
import authenticate_text
import time

inputs = ["vector 1"]
outputs = []


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


# testing encoding and decoding (without CRT):
print("\ntesting encoding and decoding (without CRT):\n")
outputs = []

startTimeWithoutCRT = time.time()

for input in inputs:
    encodedMessage = encode_text.main(True, input)
    decodedMessage = decode_text.main(True, encodedMessage, True)
    print("")
    outputs.append(decodedMessage)

# measuring Execution time of encoding and decoding without CRT
endTimeWithoutCRT = time.time()
elapsedTimeWithoutCRT = endTimeWithoutCRT - startTimeWithoutCRT

print("Initial test vector: ")
print(inputs)

print("Deciphered output: ")
print(outputs)


# testing encoding and decoding (with CRT):
print("\ntesting encoding and decoding (with CRT):\n")
outputs = []

startTimeWithCRT = time.time()

for input in inputs:
    encodedMessage = encode_text.main(True, input)
    decodedMessage = decode_text.main(True, encodedMessage, False)
    print("")
    outputs.append(decodedMessage)

# measuring Execution time of encoding and decoding with CRT
endTimeWithCRT = time.time()
elapsedTimeWithCRT = endTimeWithCRT - startTimeWithCRT

print("Initial test vector: ")
print(inputs)

print("Deciphered output: ")
print(outputs)


# testing signing and validating (without CRT):
print("\ntesting signing and validating (without CRT):\n")
outputs = []

startTimeSignWithoutCRT = time.time()

for input in inputs:
    signedMessage = sign_text.main(True, input, False)
    validatedMessage = authenticate_text.main(True, signedMessage)
    print("")
    outputs.append(validatedMessage)

endTimeSignWithoutCRT = time.time()
ellapsedTimeSignWithoutCRT = endTimeSignWithoutCRT - startTimeSignWithoutCRT

print("Initial test vector: ")
print(inputs)

print("Validated output: ")
print(outputs)


# testing signing and validating (with CRT):
print("\ntesting signing and validating (with CRT):\n")
outputs = []

startTimeSignWithCRT = time.time()

for input in inputs:
    signedMessage = sign_text.main(True, input, True)
    validatedMessage = authenticate_text.main(True, signedMessage)
    print("")
    outputs.append(validatedMessage)

endTimeSignWithCRT = time.time()
ellapsedTimeSignWithCRT = endTimeSignWithCRT - startTimeSignWithCRT

print("Initial test vector: ")
print(inputs)

print("Validated output: ")
print(outputs)

# print all Execution Time
print('Execution time of encoding and decoding without CRT:',
      elapsedTimeWithoutCRT, 'seconds')
print('Execution time of encoding and decoding with CRT:',
      elapsedTimeWithCRT, 'seconds')

print('Execution time of signing without CRT:',
      ellapsedTimeSignWithoutCRT, 'seconds')

print('Execution time of signing with CRT:',
      ellapsedTimeSignWithCRT, 'seconds')

# def test_output():
#     assert outputs, "Should be ['vector 1', 'Vector 2', 'Vector 3']"
#     print("Everything is passed")
