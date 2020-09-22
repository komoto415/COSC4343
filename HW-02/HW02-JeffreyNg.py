import sys

from typing import List, Dict, Callable

BLOCKIFY_LIST: Callable = "".join

class RC4:
    S: List[int] = []
    K: List[chr] = []

    def __init__(self, key: str):
        """
        Generating arrays for required for the key stream generation

        :param key: Key input to be spread
        :type key: str
        """
        for i in range(256):
            self.S.append(i)
            self.K.append(key[i % len(key)])

        j: int = 0
        for i in range(256):
            j = (j + self.S[i] + ord(self.K[i])) % 256
            self.swap(i, j)

    def key_gen(self, msg: str) -> List[int]:
        """
        Algorithm for spreading the key to the length of the message

        :param msg: The message that we are generating the key stream for
        :type msg: str
        :return The newly generated key stream
        :rtype: List[int]
        """
        i: int
        j: int
        i = j = 0
        key_stream: [int] = []
        for _ in msg:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.swap(i, j)
            t: int = (self.S[i] + self.S[j]) % 256
            key_stream.append(t)

        return key_stream

    def swap(self, i: int, j: int) -> None:
        """
        Swaps the values at index i and j

        :param i: index i
        :param j: index j
        :type i: int
        :type j: int
        :return: Nothing
        """
        self.S[i], self.S[j] = self.S[j], self.S[i]

def pad_char(ch: chr, ch_key: int) -> chr:
    """
    Takes a character and an integer and xor's the ASCII value of the character with the integer and returns
    the character of the xor'ed

    :param ch: Character to xor
    :param ch_key: Integer to xor the character by
    :type ch: chr
    :type ch_key: int
    :return: The character of the xor'ed integer value
    :rtype: chr
    """
    ch_i_ascii: int = ord(ch)
    xored: int = ch_i_ascii ^ int(ch_key)
    return chr(xored)

def one_time_pad(msg: str, key: List[int]) -> str:
    """
    Takes in a message and applies a xor to each character with each value of the key list

    :param msg: The message that you want to encrypt/decrypt
    :param key: The key required to encrypt/decrypt the message
    :type msg: str
    :type key: List[int]
    :return: One-time padded message
    :rtype: str
    """
    encrypted_char_list: List[chr] = [pad_char(ch, ch_key) for ch, ch_key in zip(msg, key)]
    return BLOCKIFY_LIST(encrypted_char_list)

def one_time_pad_menu() -> None:
    """
    Simple menu that asks for the message you want to encrypt and the key that will be used to encrypt the message
    with. Will require you retype in a different key if the key inputted is not the same length as the message.

    :return: Nothing
    """
    print("*****ONE-TIME PAD*****")
    msg_in: str = input("What message would you like to encrypt?\n").strip()
    same_length: bool = False
    while not same_length:
        key_in: str = input("What would you like to use as your key?\n").strip()
        same_length = len(key_in) == len(msg_in)
        if same_length:
            key_bin_list: List[int] = [ord(ch) for ch in key_in]
            encrypted_msg = one_time_pad(msg_in, key_bin_list)
            decrypted_msg = one_time_pad(encrypted_msg, key_bin_list)
            check(msg_in, encrypted_msg, decrypted_msg)
        else:
            print("Your key must be the same length as your message! Please pick a different key")
            print(f"Message Length: {len(msg_in)} :: Key Length: {len(key_in)}")
    else:
        print("*****One-Time Pad Completed*****")

def rc4_menu() -> None:
    """
    Simple menu that asks for the message you want to encrypt and the key you want to use to generate a key stream

    :return: Nothing
    """
    print("*****RC4*****")
    msg_in: str = input("What message would you like to encrypt?\n").strip()
    key_in: str = input("What would you like to use as your key?\n").strip()
    rc4_encryption: RC4 = RC4(key_in)
    key: List[int] = rc4_encryption.key_gen(msg_in)
    encrypted_msg: str = one_time_pad(msg_in, key)
    decrypted_msg: str = one_time_pad(encrypted_msg, key)
    check(msg_in, encrypted_msg, decrypted_msg)
    print("*****RC4 Completed*****")

def check(msg: str, encrypted_msg: str, decrypted_msg: str) -> None:
    """
    Simple print outs to compare the input and outputs for the user to see

    :param msg: The original string
    :param encrypted_msg: The encrypted string
    :param decrypted_msg: The decrypted string
    :type msg: str
    :type encrypted_msg: str
    :type decrypted_msg: str
    :return: Nothing
    """
    print()
    print("-" * 50)
    print("Checking matching")
    print(f"Your ciphertext:\n{encrypted_msg}")
    print("-" * 50)
    print(f"Ciphertext decrypted:\n{decrypted_msg}")
    print("-" * 50)
    print(f"The original message:\n{msg}")
    print("-" * 50)

DEFAULT_USER_RESP: int = -1
EXIT_CODE: int = 3

MENU_FETCH: Dict[int, Callable] = {
    1: one_time_pad_menu,
    2: rc4_menu,
    3: sys.exit,
    }

def main():
    state: int = 0
    user_resp: int = DEFAULT_USER_RESP
    while user_resp is not EXIT_CODE:
        if state != 0:
            print()
        print("""Welcome to my awesome encryption program
        1) One-Time Pad
        2) RC4
        3) Exit""")
        state = 1
        try:
            user_resp: int = int(input("Please pick an option: ").strip())
            if user_resp < 1 or user_resp > 3:
                print(f"That is not a valid menu option\n")
                continue
        except ValueError as e:
            print(f"Error: {e}\nPlease type an integer value\n")
        else:
            MENU_FETCH.get(user_resp)()

if __name__ == "__main__":
    main()
