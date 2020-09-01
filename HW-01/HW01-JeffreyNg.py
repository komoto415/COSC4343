import sys

PLAINTEXT_PATH: str = "plaintext.txt"
CIPHERTEXT_PATH: str = "./ciphertext.txt"

UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97
CHAR_SET_SIZE = 26

def encrypt_file():
    n_shift: int = -1
    while n_shift is -1:
        try:
            n_shift = int(input("How much do you want to shift for your encryption? ").strip())
        except ValueError as e:
            print(f"Error: {e}")
        else:
            encrypt(n_shift)

def decrypt_file():
    n_shift: int = -1
    while n_shift is -1:
        try:
            n_shift = int(input("How much do you want to shift for your decryption? ").strip())
        except ValueError as e:
            print(f"Error: {e}")
        else:
            decrypt(n_shift * -1)

def encrypt(n: int = 0):
    with open(PLAINTEXT_PATH, "r") as plaintext_file:
        lines: list = plaintext_file.readlines()
        lines_blockified: list = [x.replace("\n", "").replace(" ", "").strip() for x in lines]
        single_str: str = "".join(lines_blockified)
        shifted: str = "".join([shift(ch, n) for ch in single_str])
        with open(CIPHERTEXT_PATH, "w+") as ciphertest_file:
            ciphertest_file.write(shifted)

def decrypt(n: int = 0):
    with open(CIPHERTEXT_PATH, "r") as ciphertest_file:
        lines: list = ciphertest_file.readlines()
        with open(PLAINTEXT_PATH, "a+") as plaintext_file:
            plaintext_file.write('\n')
            plaintext_file.write('\n')
            for line in lines:
                new_line: str = "".join([shift(ch, n) for ch in line])
                plaintext_file.write(new_line)
                plaintext_file.write('\n')

def break_chipher():
    print("Chose break_chipher")

def shift(ch: str, n: int):
    if not ch.isalpha():
        return ch
    ch_as_ascii: int = ord(ch) - (UPPERCASE_OFFSET if ch.isupper() else LOWERCASE_OFFSET)
    ch_as_ascii += n
    ch_as_ascii %= CHAR_SET_SIZE
    return chr(ch_as_ascii + (UPPERCASE_OFFSET if ch.isupper() else LOWERCASE_OFFSET))

MENU_FETCH = {
    1: encrypt_file,
    2: decrypt_file,
    3: break_chipher,
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

    user_option = -1
    while user_option is not 4:
        print("""Welcome to my awesome encryption program
    1) Encrypt
    2) Decrypt
    3) Break
    4) Exit""")
        try:
            user_option = int(input("Please pick an option: ").strip())
            if user_option < 1 or user_option > 4:
                print(f"That is not a valid option\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\n")
        else:
            MENU_FETCH.get(user_option)()
        print()

if __name__ == "__main__":
    main()
