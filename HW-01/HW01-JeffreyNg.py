import sys
from typing import List, Dict, Callable, Tuple

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

def job_using_shift(user_resp: int) -> None:
    """
    Determines whether the user wants to decrypt or encrypt based on selected response and asks for the desired key
    shift value to perform said job

    :param user_resp: the selected menu value
    :type user_resp: int
    :return: None
    :raises ValueError: if attempted user input is not an integer literal
    """
    job_done: bool = False
    option_name: str = ["encrypt", "decrypt"][user_resp - 1]
    while not job_done:
        try:
            n_shift: int = int(input(f"How much do you want to shift for your {option_name}ion? ").strip())
            if n_shift < 1 or n_shift > 25:
                print(f"Your shift must be between 1 and 25\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\nPlease type an integer value")
        else:
            globals()[option_name](n_shift)
            job_done = True
            print(f"{option_name[0].upper()}{option_name[1:]}ion complete")

def encrypt(n: int = 0) -> None:
    """
    Reads plaintext.txt then encrypts its content with the key shift n and writes the encrypted message to
    ciphertext.txt

    :param n: the key shift
    :type n: int
    :return: None
    """
    with open(PLAINTEXT_PATH, "r") as plaintext_file:
        lines: List[str] = plaintext_file.readlines()
        single_block_str: str = STRINGIFY_LIST(lines).replace('\n', '').replace(' ', '').strip()
        shifted: str = STRINGIFY_LIST([shift(ch, n) for ch in single_block_str])
    with open(CIPHERTEXT_PATH, "w+") as ciphertext_file:
        ciphertext_file.write(shifted)

def decrypt(n: int = 0) -> None:
    """
    Reads ciphertext.txt then decrypts its content with the key shift n and writes the decrypted message to
    plaintext.txt

    :param n: the key shift
    :type n: int
    :return: None
    """
    n *= -1
    with open(CIPHERTEXT_PATH, "r") as ciphertext_file:
        lines: List[str] = ciphertext_file.readlines()
    with open(PLAINTEXT_PATH, "w+") as plaintext_file:
        for i, line in enumerate(lines, 1):
            new_line: str = STRINGIFY_LIST([shift(ch, n) for ch in line])
            plaintext_file.write(new_line)
            # Just ensures file has no trailing new line
            if i != len(lines):
                plaintext_file.write('\n')

def lazy_search_and_ask(_) -> None:
    """
    Goes all potential shifts and asks the user if it's the correct one

    :param _:
    :return: None
    """
    with open(CIPHERTEXT_PATH) as ciphertext_file:
        lines: List[str] = ciphertext_file.readlines()
    lines_as_single_str: str = ''.join([line for line in lines if line != '\n']).strip()

    i: int = 1
    key_found: bool = False
    while i <= 26 and not key_found:
        well_formed_input: bool = False
        if i != 0:
            print()
        print(f"Testing Key Shift: {i}")
        cipher_shifted_by_i: str = STRINGIFY_LIST([shift(ch, i*-1) for ch in lines_as_single_str])
        print(f"Below is the text using the key shift {i}")
        print(cipher_shifted_by_i)
        while not well_formed_input:
            resp: str = input("Was this the correct shift? (Y/N): ").upper().strip()
            key_found = resp == "Y"
            well_formed_input = resp == "Y" or resp == "N"
        i += 1

def range_fixing_ascii_range(ch: str, offset: int) -> int:
    """
    Converts an english alphabetic character into it's ASCII code and offsets it to sit in a range of 0-25

    :param ch: the character being converted into ASCII
    :param offset: ASCII casing offset to fixed in 0-25 range
    :type ch: chr
    :type offset: int
    :return: the range fixed ASCII value
    :raises: ValueError: if the character attempting to fixed doesn't have an ASCII code
    """
    if not ch.isascii():
        raise ValueError("The character you are trying fix is not an ASCII character")
    return ord(ch) - offset

def shift(ch: chr, n: int) -> chr:
    """
    Shifts an english alphabetic character n number times

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

    casing_offset: int = UPPERCASE_ASCII_OFFSET if ch.isupper() else LOWERCASE_ASCII_OFFSET
    ch_range_fixed: int = range_fixing_ascii_range(ch, casing_offset)
    ch_range_fixed += n
    ch_range_fixed %= CHAR_SET_SIZE
    return chr(ch_range_fixed + casing_offset)

MENU_FETCH: Dict[int, Callable] = {
    1: job_using_shift,
    2: job_using_shift,
    3: lazy_search_and_ask,
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
        with open(PLAINTEXT_PATH) as _:
            pass
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Creating {PLAINTEXT_PATH} and writing in: {DEFAULT_PLAINTEXT_WRITE}\n")
        with open(PLAINTEXT_PATH, "w") as plaintext_file:
            plaintext_file.write(DEFAULT_PLAINTEXT_WRITE)

    try:
        with open(CIPHERTEXT_PATH) as _:
            pass
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Creating {CIPHERTEXT_PATH} and writing in: {DEFAULT_CIPHERTEXT_WRITE}\n")
        with open(CIPHERTEXT_PATH, "w") as ciphertext_file:
            ciphertext_file.write(DEFAULT_CIPHERTEXT_WRITE)

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
                print(f"That is not a valid menu option\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\nPlease type an integer value\n")
        else:
            MENU_FETCH.get(user_resp)(user_resp)
        print()

if __name__ == "__main__":
    main()
