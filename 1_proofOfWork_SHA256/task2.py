from common import generate_nonce, Sha256
from tqdm import tqdm

# Read input text from a file
input_file_path = "input.txt"  # Replace with the actual path to your input file
with open(input_file_path, "r") as file:
    input_text = file.read()

difficulty_level = 20
print("Computing...")
pbar = tqdm(total=None)
while True:
    # Generate a random nonce
    nonce = generate_nonce()

    # Append the nonce to the input text
    in_text_with_nonce = f"{input_text}{nonce}"

    secure_hash = Sha256(in_text_with_nonce).hexdigest()
    # convert secure_hash to binary and print it properly with 4 bits grouped 
    bin_secure_hash = bin(int(secure_hash, 16))[2:].zfill(256)
    
   
    #  check difficulty l
    if bin_secure_hash[:difficulty_level] == "0" * difficulty_level:
        
        print(
            f"Nonce: {nonce} \n Secure Hash (SHA-256): {secure_hash} \n Binary Secure Hash: {bin_secure_hash} \n Difficulty Level: {difficulty_level}\n "
        )
        break
    pbar.update(1)

pbar.close()
