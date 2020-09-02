import unittest
import importlib
from typing import List

HW = importlib.import_module("HW01-JeffreyNg")

def format_file_as_single_str(ext_file: str) -> str:
    with  open(ext_file, "r") as test_file:
        lines: List[str] = test_file.readlines()
        return '\n'.join(['\n' if line is ' ' else line.strip() for line in lines])

def init(file: str, write_me: str):
    with open(HW.PLAINTEXT_PATH if file is "plaintext.txt" else HW.CIPHERTEXT_PATH) as _:
        pass
    with open(file, "w") as f:
        for ch in write_me:
            f.write(ch)

def get_written(file: str):
    with open(file, "r") as f:
        lines: List[str] = f.readlines()
        ret: List[str] = []
        for line in lines:
            aux = line
            if line is ' ':
                aux = '\n'
            ret.append(aux)
        return " ".join(ret)

class MyTestCase(unittest.TestCase):

    def test_b_caesar_shift_helloworld(self):
        test_str = "helloworld"
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.encrypt(shift)
        actual: str = get_written(HW.CIPHERTEXT_PATH)
        expected: str = "khoorzruog"
        self.assertEqual(expected, actual)

    def test_c_decrypt_caesar_back_to_helloworld(self):
        test_str = "khoorzruog"
        init(HW.CIPHERTEXT_PATH, test_str)
        shift = 3
        HW.decrypt(shift)
        actual: str = get_written(HW.PLAINTEXT_PATH)
        expected: str = "helloworld"
        self.assertEqual(expected, actual)

    def test_d_caesar_shift_steds(self):
        test_str = "St. Edward's University"
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.encrypt(shift)
        actual: str = get_written(HW.CIPHERTEXT_PATH)
        expected: str = "Vw.Hgzdug'vXqlyhuvlwb"
        self.assertEqual(expected, actual)

    def test_e_decrypt_caesar_back_to_steds(self):
        test_str = "Vw.Hgzdug'vXqlyhuvlwb"
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.decrypt(shift)
        actual: str = get_written(HW.PLAINTEXT_PATH)
        expected: str = "St.Edward'sUniversity"
        self.assertEqual(expected, actual)

    def test_f_caesar_shift_steds_newlines(self):
        test_str = "St.\n\n\nEdward's\n\n University"
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.encrypt(shift)
        actual: str = get_written(HW.CIPHERTEXT_PATH)
        expected: str = "Vw.Hgzdug'vXqlyhuvlwb"
        self.assertEqual(expected, actual)

    def test_g_caesar_shift_my_name(self):
        test_str = "Jeffrey Ng"
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.encrypt(shift)
        actual: str = get_written(HW.CIPHERTEXT_PATH)
        expected: str = "MhiiuhbQj"
        self.assertEqual(expected, actual)

    def test_h_decrypt_caesar_back_to_my_name(self):
        test_str = "MhiiuhbQj"
        init(HW.CIPHERTEXT_PATH, test_str)
        shift = 3
        HW.decrypt(shift)
        actual: str = get_written(HW.PLAINTEXT_PATH)
        expected: str = "JeffreyNg"
        self.assertEqual(expected, actual)

    def test_a_ext_write(self):
        test_file: str = "test_1.txt"
        actual: str = format_file_as_single_str(test_file)
        expected: str = "I Love\nthe ABC's\n\nWhat about you?"
        self.assertEqual(expected, actual)

    def test_i_caeser_test_file_1(self):
        test_str = format_file_as_single_str("test_1.txt")
        init(HW.PLAINTEXT_PATH, test_str)
        shift = 3
        HW.encrypt(shift)
        actual: str = get_written(HW.CIPHERTEXT_PATH)
        expected: str = "LOryhwkhDEF'vZkdwderxwbrx?"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
