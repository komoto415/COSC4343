import sys
from typing import List, Dict, Callable

PLAINTEXT_PATH: str = "plaintext.txt"
CIPHERTEXT_PATH: str = "ciphertext.txt"

UPPERCASE_ASCII_OFFSET: int = 65
LOWERCASE_ASCII_OFFSET: int = 97
CHAR_SET_SIZE: int = 26
DEFAULT_USER_RESP: int = -1
EXIT_CODE: int = 4
STRINGIFY_LIST: Callable = "".join

DEFAULT_PLAINTEXT_WRITE: str = "helloworld"
DEFAULT_CIPHERTEXT_WRITE: str = "khoorzruog"


def shift_option(user_resp: int) -> None:
    job_done: bool = False
    option_name: str = ["encrypt", "decrypt"][user_resp - 1]
    while not job_done:
        try:
            n_shift: int = int(input(f"How much do you want to shift for your {option_name}ion? ").strip())
        except ValueError as e:
            print(f"Error: {e}")
        else:
            globals()[option_name](n_shift)
            job_done = True

def encrypt(n: int = 0) -> None:
    with open(PLAINTEXT_PATH, "r") as plaintext_file:
        lines: List[str] = plaintext_file.readlines()
        single_block_str: str = STRINGIFY_LIST(lines).replace('\n', '').replace(' ', '').strip()
        shifted: str = STRINGIFY_LIST([shift(ch, n) for ch in single_block_str])
        with open(CIPHERTEXT_PATH, "w+") as ciphertext_file:
            ciphertext_file.write(shifted)

def decrypt(n: int = 0) -> None:
    """
    Reads and decrypts ciphertext.txt and writes the decrypted message to plaintext.txt

    :param n: the key shift
    :type n: int
    :return: None
    """
    n *= -1
    with open(CIPHERTEXT_PATH, "r") as ciphertext_file:
        lines: List[str] = ciphertext_file.readlines()
        with open(PLAINTEXT_PATH, "w+") as plaintext_file:
            # plaintext_file.write('\n')
            # plaintext_file.write('\n')
            for i, line in enumerate(lines, 1):
                new_line: str = STRINGIFY_LIST([shift(ch, n) for ch in line])
                plaintext_file.write(new_line)
                # Just ensures file has no trailing new line
                if i is not len(lines):
                    plaintext_file.write('\n')

def break_cipher(_):
    print("Chose break_chipher")

def shift(ch: chr, n: int) -> chr:
    """
    Shifts an english alphabetic  character n number times

    :param ch: the character being shifted
    :param n: the key shift
    :type ch: chr
    :type n: int
    :return: the shifted character
    :rtype: chr
    :raises: TypeError: if the ch is not a character
    """
    try:
        ord(ch)
    except TypeError as e:
        print(f"Error: {e}")
        raise

    if not ch.isalpha():
        return ch
    # Offset ascii value to to 0-25 range
    casing_offset: int = UPPERCASE_ASCII_OFFSET if ch.isupper() else LOWERCASE_ASCII_OFFSET
    ch_zeroed_range: int = ord(ch) - casing_offset
    ch_zeroed_range += n
    ch_zeroed_range %= CHAR_SET_SIZE
    return chr(ch_zeroed_range + casing_offset)

MENU_FETCH: Dict[int, Callable] = {
    1: shift_option,
    2: shift_option,
    3: break_cipher,
    4: sys.exit,
    }

'''
The Gettysburg Address

Four score and seven years ago our fathers brought forth on this continent, a new nation,
conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so
conceived and so dedicated, can long endure. We are met on a great battle field of that war.
We have come to dedicate a portion of that field, as a final resting place for those who here
gave their lives that that nation might live. It is altogether fitting and proper that we should do
this.

But, in a larger sense, we can not dedicate-we can not consecrate-we can not hallow-this
ground. The brave men, living and dead, who struggled here, have consecrated it, far above our
poor power to add or detract. The world will little note, nor long remember what we say here,
but it can never forget what they did here. It is for us the living, rather, to be dedicated here to
the unfinished work which they who fought here have thus far so nobly advanced. It is rather
for us to be here dedicated to the great task remaining before us-that from these honored
dead we take increased devotion to that cause for which they gave the last full measure of
devotion-that we here highly resolve that these dead shall not have died in vain-that this
nation, under God, shall have a new birth of freedom-and that government of the people, by
the people, for the people, shall not perish from the earth.

Abraham Lincoln.

November 19, 1863
'''

def main():
    try:
        with open(CIPHERTEXT_PATH) as _:
            pass
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Creating {CIPHERTEXT_PATH} and writing in '{DEFAULT_CIPHERTEXT_WRITE}'")
        with open(CIPHERTEXT_PATH, "w") as ciphertext_file:
            ciphertext_file.write(DEFAULT_CIPHERTEXT_WRITE)
            pass

    try:
        with open(PLAINTEXT_PATH) as _:
            pass
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Creating {PLAINTEXT_PATH} and writing in '{DEFAULT_PLAINTEXT_WRITE}'")
        with open(PLAINTEXT_PATH, "w") as plaintext_file:
            plaintext_file.write(DEFAULT_PLAINTEXT_WRITE)

    user_resp = DEFAULT_USER_RESP
    while user_resp is not EXIT_CODE:
        print("""Welcome to my awesome encryption program
    1) Encrypt
    2) Decrypt
    3) Break
    4) Exit""")
        try:
            user_resp: int = int(input("Please pick an option: ").strip())
            if user_resp < 1 or user_resp > 4:
                print(f"That is not a valid option\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\n")
        else:
            MENU_FETCH.get(user_resp)(user_resp)
        print()

if __name__ == "__main__":
    main()
