import time
from common import generate_nonce, Sha256, generate_secure_hash

# Read input text from a file
input_file_path = "input.txt"  # Replace with the actual path to your input file
with open(input_file_path, "r") as file:
    input_text = file.read()

# Generate a random nonce
nonce = generate_nonce(length=32)

# Append the nonce to the input text
input_text_with_nonce = f"{input_text}{nonce}"


start_time = time.time()
secure_hash = Sha256(input_text_with_nonce).hexdigest()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to generate the secure hash(my function): {elapsed_time} seconds")

start_time = time.time()
secure_hash_lib = generate_secure_hash(input_text_with_nonce)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to generate the secure hash(lib function): {elapsed_time} seconds")

# Print the results
print(f"Input Text: {input_text}")
print(f"Nonce: {nonce}")
print(f"Input Text with Nonce: {input_text_with_nonce}")
print(f"Secure Hash (SHA-256) - my function: {secure_hash}")
print(f"Secure Hash (SHA-256) - Lib functon: {secure_hash_lib}")
print(f"Length of Secure Hash: {len(secure_hash)}")
