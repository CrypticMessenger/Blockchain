from common import Sha256


class MerkleTree:
    def __init__(self, transactions):
        # transactions: list of transactions
        # tree: list of lists of hashes, starting from the bottom level
        self.transactions = transactions
        self.tree = self.build_tree()

    def build_tree(self):
        # if the number of transactions is odd, duplicate the last transaction
        if len(self.transactions) % 2 != 0:
            self.transactions.append(self.transactions[-1])

        # start with the bottom level of the tree
        tree = [
            [
                Sha256(transaction.encode()).hexdigest()
                for transaction in self.transactions
            ]
        ]

        # build the rest of the tree level by level, lv is the current level
        lv = 0

        # while the current level has more than one node i.e. the root is not reached
        while len(tree[-1]) > 1:
            # if the number of nodes in the current level is odd, duplicate the last node
            if len(tree[lv]) % 2 != 0:
                tree[lv].append(tree[lv][-1])

            # create the next level by hashing the concatenation of each pair of nodes, and calculating hash of the result
            new_lv = [
                Sha256(
                    tree[lv][i].encode() + tree[lv][i + 1].encode()
                ).hexdigest()
                for i in range(0, len(tree[lv]), 2)
            ]

            tree.append(new_lv)
            lv += 1
        # return the tree
        return tree

    def get_root(self):
        return self.tree[-1][0]

    def get_proof(self, transaction):
        # if the transaction is not in the list of transactions, return an empty list
        if transaction not in self.transactions:
            return []
        index = self.transactions.index(transaction)

        # imp_nodes is a list of important nodes in the tree that are needed to verify the transaction
        imp_nodes = [[self.tree[0][index], 0]]
        lv = 0

        # while the current level has more than one node i.e. the root is not reached
        # Append 1 or -1 to the imp_nodes list to indicate the position of the node in the next level
        # since position matters while calculating the hash, 1 means the node is on the right, -1 means the node is on the left
        while len(self.tree[lv]) > 1:
            if index % 2 == 0:
                imp_nodes.append([self.tree[lv][index + 1], 1])
            else:
                imp_nodes.append([self.tree[lv][index - 1], -1])
            index = index // 2
            lv += 1

        return imp_nodes

    def verify_proof(self, proof):
        # if the proof is empty, return False
        if len(proof) == 0:
            return False
        next_hash = proof[0][0]
        # calculate the hash of the concatenation of the important nodes in the proof
        # and utilize the position of the nodes to calculate the hash
        for i in range(1, len(proof)):
            relative_position = proof[i][1]
            if relative_position == -1:
                next_hash = Sha256(
                    proof[i][0].encode() + next_hash.encode()
                ).hexdigest()
            else:
                next_hash = Sha256(
                    next_hash.encode() + proof[i][0].encode()
                ).hexdigest()

        # return True if the calculated hash is equal to the root of the tree
        return next_hash == self.get_root()
