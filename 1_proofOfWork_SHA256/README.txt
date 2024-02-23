- first run `pip3 install -r requirements.txt` to install required packages.

# Task1.py
- To run the program, type `python3 task1.py` in the terminal.
- It should print hash values of given strings calculated  by my hash function and python's hash function, along with time elaspsed.
- The hash values should be same, to verify correctness of my hash function.

# Task2.py
- To run the program, type `python3 task2.py` in the terminal.
- It should show progress of the program using tqdm and time elaspsed.
- When program finds the appropriate nonce and hash value, the program halts and prints the nonce and hash value.

# utility.py
- This file contains utility functions used in common.py 

# common.py
- This file contains common functions used in task1.py and task2.py

# References:
- I followed this article: https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/ to implement SHA256.