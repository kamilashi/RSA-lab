# RSA-lab

This is a simple implementation of RSA algorithm with different key lengths (1024, 2048 and 4096 bits). 
The solution can be run with and without the Chinese Remainder Theorem (CRT).

Please follow the steps to run the script:

1. Go the file `test_with_vectors.py`
2. Paste your text to test into a variable `input` inside this file 
3. Run the python script `python3 test_with_vectors.py`
4. You should be able to see the terminal output with inital vector and decoded result as well as perforamnce measures

By default the script runs all possible combinations:
* Encoding without CRT
* Decoding wihout CRT
* Encoding with CRT
* Decoding with CRT
* Signing and Veryfication with and without CRT

You can also test key generation only. For this purpose please follow the steps:

1. Go the file `generate_keys.py`
2. If you'd like you can change key length by changing vatiable `length` (default value is `1024 bit`)
3. Run the python script `python3 generate_keys.py`
4. You should be able to see the terminal output with gererated keys `n`,`e`,`d` and intermediate values `p`, `q`, `phi`
