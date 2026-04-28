import unittest
from src.gen_content import extract_title

class TestGenContent(unittest.TestCase):
    def test_simple_h1(self):
        res = extract_title('# Hello')
        self.assertEqual(res, 'Hello')

    def test_h1_not_on_first_line(self):
        res = extract_title('## I feel so lonesome\n ### smoke and nicotine\n feeelinggg so lonely\n# Hello #World!')
        self.assertEqual(res, 'Hello #World!')

    def no_h1_found(self):
        with self.assertRaises(Exception):
            extract_title('no titles are in this string\n #### SIIIIR! ')