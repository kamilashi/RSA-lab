import decode_text
import encode_text
import sign_text
import authenticate_text
import generate_keys
import time


def printAverageTime(arr, funName):
    avrg = sum(arr) / len(arr)
    print(f"Average time taken for {funName}: {avrg:.4f}")


inputs = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
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
print(f"key length {generate_keys.length} bit")
print(f"Text length: {len(inputs[0])}")
print("\ntesting encoding and decoding (without CRT):\n")
outputs = []

encodeTimeWithoutCRT = []
decodeTimeWithoutCRT = []

for input in inputs:
    startTimeEncodeWithoutCRT = time.time()
    encodedMessage = encode_text.main(True, input)
    endTimeEncodeWithoutCRT = time.time()

    elapsedTimeWithoutCRT = endTimeEncodeWithoutCRT - startTimeEncodeWithoutCRT
    encodeTimeWithoutCRT.append(elapsedTimeWithoutCRT)

    startTimeDecodeWithoutCRT = time.time()
    decodedMessage = decode_text.main(True, encodedMessage, False)
    endTimeDecodeWithoutCRT = time.time()
    elapsedTimeDecodeWithoutCRT = endTimeDecodeWithoutCRT - startTimeDecodeWithoutCRT
    decodeTimeWithoutCRT.append(elapsedTimeDecodeWithoutCRT)

    print("")
    outputs.append(decodedMessage)

# print("Initial test vector: ")
# print(inputs)

# print("Deciphered output: ")
# print(outputs)

printAverageTime(encodeTimeWithoutCRT, "Encryption without CRT")
printAverageTime(decodeTimeWithoutCRT, "Decryption without CRT")


# testing encoding and decoding (with CRT):
print("\ntesting encoding and decoding (with CRT):\n")
outputs = []

encodeTimeWithCRT = []
decodeTimeWithCRT = []

for input in inputs:
    startTimeEncodeWithCRT = time.time()
    encodedMessage = encode_text.main(True, input)
    endTimeEncodeWithCRT = time.time()

    elapsedTimeEncodeWithCRT = endTimeEncodeWithCRT - startTimeEncodeWithCRT
    encodeTimeWithCRT.append(elapsedTimeEncodeWithCRT)

    startTimeDecodeWithCRT = time.time()
    decodedMessage = decode_text.main(True, encodedMessage, True)
    endTimeDecodeWithCRT = time.time()

    elapsedTimeDecodeWithCRT = endTimeDecodeWithCRT - startTimeDecodeWithCRT
    decodeTimeWithCRT.append(elapsedTimeDecodeWithCRT)

    print("")
    outputs.append(decodedMessage)


# print("Initial test vector: ")
# print(inputs)

# print("Deciphered output: ")
# print(outputs)

printAverageTime(encodeTimeWithCRT, "Encryption with CRT")
printAverageTime(decodeTimeWithCRT, "Decryption with CRT")


# testing signing and validating (without CRT):
print("\ntesting signing and validating (without CRT):\n")
outputs = []
signTimeWithoutCRT = []
validateTimeWithoutCRT = []

for input in inputs:
    startTimeSignWithoutCRT = time.time()
    signedMessage = sign_text.main(True, input, False)
    endTimeSignWithoutCRT = time.time()

    ellapsedTimeSignWithoutCRT = endTimeSignWithoutCRT - startTimeSignWithoutCRT
    signTimeWithoutCRT.append(ellapsedTimeSignWithoutCRT)

    startTimeValidateWithoutCRT = time.time()
    validatedMessage = authenticate_text.main(True, signedMessage)
    endTimeValidateWithoutCRT = time.time()

    ellapsedTimeValidateWithoutCRT = endTimeValidateWithoutCRT - \
        startTimeValidateWithoutCRT
    validateTimeWithoutCRT.append(ellapsedTimeValidateWithoutCRT)

    print("")
    outputs.append(validatedMessage)


# print("Initial test vector: ")
# print(inputs)

# print("Validated output: ")
# print(outputs)

printAverageTime(signTimeWithoutCRT, "Signing without CRT")
printAverageTime(validateTimeWithoutCRT, "Validation without CRT")


# testing signing and validating (with CRT):
print("\ntesting signing and validating (with CRT):\n")
outputs = []
signTimeWithCRT = []
validateTimeWithCRT = []

for input in inputs:
    startTimeSignWithCRT = time.time()
    signedMessage = sign_text.main(True, input, True)
    endTimeSignWithCRT = time.time()
    ellapsedTimeSignWithCRT = endTimeSignWithCRT - startTimeSignWithCRT
    signTimeWithCRT.append(ellapsedTimeSignWithCRT)

    startTimeValidateWithCRT = time.time()
    validatedMessage = authenticate_text.main(True, signedMessage)
    endTimeValidateWithCRT = time.time()

    ellapsedTimeValidateWithCRT = endTimeValidateWithCRT - \
        startTimeValidateWithCRT
    validateTimeWithCRT.append(ellapsedTimeValidateWithCRT)
    print("")
    outputs.append(validatedMessage)

# print("Initial test vector: ")
# print(inputs)

# print("Validated output: ")
# print(outputs)

printAverageTime(signTimeWithCRT, "Signing with CRT")
printAverageTime(validateTimeWithCRT, "Validation with CRT")
