
import decode_text
import encode_text

encodedMessage = encode_text.main(True, "this");
decodedMessage = decode_text.main(False, "", False);
print(encodedMessage);