import decode_text
import encode_text
import sign_text
import authenticate_text
import generate_keys

encodedMessage = encode_text.main(False);
decodedMessage = decode_text.main(False);

print(decodedMessage);