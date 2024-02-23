def pad(message_length):
    """pads the message for SHA-256 processing."""
    # Calculate the remainder of the message length divided by 64
    # Convert the message length from bytes to bits
    # Calculate the padding length
    remainder = message_length & 0x3F
    length_in_bits = (message_length << 3).to_bytes(8, "big")
    padding_length = 55 - remainder if remainder < 56 else 119 - remainder

    # Return the padded message
    return b"\x80" + b"\x00" * padding_length + length_in_bits


def rotate_right(x, y):
    return ((x >> y) | (x << (32 - y))) & 0xFFFFFFFF


def majority_fn(x, y, z):
    # return a number that has its bits set where the majority of x, y, and z have their bits set.
    return (x & y) ^ (x & z) ^ (y & z)


def choice_fn(x, y, z):
    # choice function
    return (x & y) ^ ((~x) & z)

def get_hash_values():
    # initialize hash_values
    hash_values = [
        0x6A09E667,
        0xBB67AE85,
        0x3C6EF372,
        0xA54FF53A,
        0x510E527F,
        0x9B05688C,
        0x1F83D9AB,
        0x5BE0CD19,
    ]
    return hash_values

def get_rotate_constants():
    # initialize rotate constants
    rot_constants = [
        0x428A2F98,
        0x71374491,
        0xB5C0FBCF,
        0xE9B5DBA5,
        0x3956C25B,
        0x59F111F1,
        0x923F82A4,
        0xAB1C5ED5,
        0xD807AA98,
        0x12835B01,
        0x243185BE,
        0x550C7DC3,
        0x72BE5D74,
        0x80DEB1FE,
        0x9BDC06A7,
        0xC19BF174,
        0xE49B69C1,
        0xEFBE4786,
        0x0FC19DC6,
        0x240CA1CC,
        0x2DE92C6F,
        0x4A7484AA,
        0x5CB0A9DC,
        0x76F988DA,
        0x983E5152,
        0xA831C66D,
        0xB00327C8,
        0xBF597FC7,
        0xC6E00BF3,
        0xD5A79147,
        0x06CA6351,
        0x14292967,
        0x27B70A85,
        0x2E1B2138,
        0x4D2C6DFC,
        0x53380D13,
        0x650A7354,
        0x766A0ABB,
        0x81C2C92E,
        0x92722C85,
        0xA2BFE8A1,
        0xA81A664B,
        0xC24B8B70,
        0xC76C51A3,
        0xD192E819,
        0xD6990624,
        0xF40E3585,
        0x106AA070,
        0x19A4C116,
        0x1E376C08,
        0x2748774C,
        0x34B0BCB5,
        0x391C0CB3,
        0x4ED8AA4A,
        0x5B9CCA4F,
        0x682E6FF3,
        0x748F82EE,
        0x78A5636F,
        0x84C87814,
        0x8CC70208,
        0x90BEFFFA,
        0xA4506CEB,
        0xBEF9A3F7,
        0xC67178F2,
    ]
    return rot_constants