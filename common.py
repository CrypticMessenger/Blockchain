from utility import *
import threading




class Sha256:
    def __init__(self, m=None):
        # convert m to bytes if it is a string for byte operations
        if isinstance(m, str):
            m = m.encode("utf-8")
        self.buffer = b""

        self.msg_len = 0
        # STEP 2 - INITIALIZE HASH VALUES (H)
        self.hash_values = get_hash_values()
        # STEP 3 - INITIALIZE ROUND CONSTANTS (K)
        self.rotate_cnsts = get_rotate_constants()
        self.finalized = False
        if m is not None:
            self.update(m)

    def compress(self, c):
        # Step 5: CREATE MESSAGE SCHEDULE (W)
        w = [0] * 64
        w[0:16] = [int.from_bytes(c[i : i + 4], "big") for i in range(0, len(c), 4)]

        for i in range(16, 64):
            s0 = (
                rotate_right(w[i - 15], 7)
                ^ rotate_right(w[i - 15], 18)
                ^ (w[i - 15] >> 3)
            )
            s1 = (
                rotate_right(w[i - 2], 17)
                ^ rotate_right(w[i - 2], 19)
                ^ (w[i - 2] >> 10)
            )
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        # Step 6: value intializations for compression function
        a, b, c, d, e, f, g, h = self.hash_values

        # Step 6: Compression function main loop:
        for i in range(64):
            s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
            t2 = s0 + majority_fn(a, b, c)
            s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
            t1 = h + s1 + choice_fn(e, f, g) + self.rotate_cnsts[i] + w[i]

            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF
        # step 7: MODIFY FINAL VALUES
        for i, (x, y) in enumerate(zip(self.hash_values, [a, b, c, d, e, f, g, h])):
            self.hash_values[i] = (x + y) & 0xFFFFFFFF

    def digest(self):
        if not self.finalized:
            self.update(pad(self.msg_len))
            self.digest = b"".join(x.to_bytes(4, "big") for x in self.hash_values[:8])
            self.finalized = True
        return self.digest

    def update(self, msg):
        if msg is None or len(msg) == 0:
            return

        if self.finalized:
            raise AssertionError("Hash already finalized and cannot be updated!")

        self.msg_len += len(msg)
        msg = self.buffer + msg

        # Step 4: Process message in 64-byte chunks
        num_chunks = len(msg) // 64
        threads = []

        def compress_chunk(start, end):
            for i in range(start, end):
                self.compress(msg[64 * i : 64 * (i + 1)])

        # Determine the number of threads (you can adjust this number based on your system)
        num_threads = min(4, num_chunks)

        # Adjust chunk_size based on num_chunks and num_threads
        if num_threads < num_chunks:
            chunk_size = num_chunks // num_threads
        else:
            chunk_size = 1
            num_threads = num_chunks

        # Divide the work among threads
        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i != num_threads - 1 else num_chunks
            thread = threading.Thread(target=compress_chunk, args=(start, end))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        self.buffer = msg[len(msg) - (len(msg) % 64) :]

    def hexdigest(self):
        # convert bytes to hex
        tab = "0123456789abcdef"
        return "".join(tab[b >> 4] + tab[b & 0xF] for b in self.digest())
