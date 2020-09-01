import sys
from typing import List, Dict, Callable

PLAINTEXT_PATH: str = "plaintext.txt"
CIPHERTEXT_PATH: str = "ciphertext.txt"

UPPERCASE_ASCII_OFFSET: int = 65
LOWERCASE_ASCII_OFFSET: int = 97
CHAR_SET_SIZE: int = 26
DEFAULT_USER_RESP: int = -1

def shift_option(user_option: int) -> None:
    job_done: bool = False
    option_name: str = ["encrypt", "decrypt"][user_option - 1]
    while not job_done:
        try:
            n_shift: int = int(input(f"How much do you want to shift for your {option_name}ion? ").strip())
        except ValueError as e:
            print(f"Error: {e}")
        else:
            if option_name is "decrypt":
                n_shift *= -1
            globals()[option_name](n_shift)
            job_done = True

def encrypt(n: int = 0) -> None:
    with open(PLAINTEXT_PATH, "r") as plaintext_file:
        lines: List[str] = plaintext_file.readlines()
        single_str: str = "".join(lines).replace('\n', '').replace(' ', '').strip()
        shifted: str = "".join([shift(ch, n) for ch in single_str])
        with open(CIPHERTEXT_PATH, "w+") as ciphertext_file:
            ciphertext_file.write(shifted)

def decrypt(n: int = 0) -> None:
    with open(CIPHERTEXT_PATH, "r") as ciphertext_file:
        lines: List[str] = ciphertext_file.readlines()
        with open(PLAINTEXT_PATH, "a+") as plaintext_file:
            plaintext_file.write('\n')
            plaintext_file.write('\n')
            for line in lines:
                new_line: str = "".join([shift(ch, n) for ch in line])
                plaintext_file.write(new_line)
                plaintext_file.write('\n')

def break_cipher(_):
    print("Chose break_chipher")

def shift(ch: str, n: int) -> chr:
    if not ch.isalpha():
        return ch
    ch_as_ascii: int = ord(ch) - (UPPERCASE_ASCII_OFFSET if ch.isupper() else LOWERCASE_ASCII_OFFSET)
    ch_as_ascii += n
    ch_as_ascii %= CHAR_SET_SIZE
    return chr(ch_as_ascii + (UPPERCASE_ASCII_OFFSET if ch.isupper() else LOWERCASE_ASCII_OFFSET))

MENU_FETCH: Dict[int, Callable] = {
    1: shift_option,
    2: shift_option,
    3: break_cipher,
    4: sys.exit,
    }

def main():
    try:
        with open(PLAINTEXT_PATH) as _:
            pass
        with open(CIPHERTEXT_PATH) as _:
            pass
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

    user_option = DEFAULT_USER_RESP
    while user_option is not 4:
        print("""Welcome to my awesome encryption program
    1) Encrypt
    2) Decrypt
    3) Break
    4) Exit""")
        try:
            user_option: int = int(input("Please pick an option: ").strip())
            if user_option < 1 or user_option > 4:
                print(f"That is not a valid option\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\n")
        else:
            MENU_FETCH.get(user_option)(user_option)
        print()

if __name__ == "__main__":
    main()
