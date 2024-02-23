from MerkleTree import MerkleTree

################################### Input ###################################
transactions = [
    "0xA_0xB_100_BTC_1",
    "0xC_0xD_200_BTC_2",
    "0xE_0xF_300_BTC_3",
    "0xG_0xH_400_BTC_4",
    "0xI_0xJ_500_BTC_5",
    "0xK_0xL_600_BTC_6",
    "0xM_0xN_700_BTC_7",
    "0xO_0xP_800_BTC_8",
    "0xQ_0xR_900_BTC_9",
    "0xS_0xT_1000_BTC_10",
    "0xU_0xV_1100_BTC_11",
]
transactions_to_prove = ["0xA_0xB_100_BTC_1", "0xX_0xZ_600_BTC_99", "0xW_0xX_12_BTC_100"]

################################### Input end ###################################


# Create a Merkle Tree
merkle_tree = MerkleTree(transactions)

print("---------------------Tree---------------------")
# Print the tree
for i, nodes in enumerate(merkle_tree.tree):
    print(f"Level {i}: ", end="")
    for node in nodes:
        print(f"{node[-10:]} ", end="")
    print()

print("\n---------------------Root---------------------")
# Print the root of the tree
print(f"Root: {merkle_tree.get_root()}")
print("\n---------------------Verifications---------------------")
# Print the verification of each transaction in list transactions_to_prove
for transaction in transactions_to_prove:
    proof = merkle_tree.get_proof(transaction)
    # print(f"Transaction: {transaction}, Proof: {proof}")
    verification = merkle_tree.verify_proof(proof)
    print(f"Transaction: {transaction}, Verification: {verification}")
