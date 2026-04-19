import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("same_text", TextType.TEXT)
        node2 = TextNode("same_text", TextType.TEXT)
        self.assertEqual(node, node2) 

    def test_ineq(self):
        node = TextNode("Text1", TextType.TEXT, "url1")
        node2 = TextNode("Text2", TextType.TEXT, "url2")
        self.assertNotEqual(node, node2)

    def test_ineq2(self):
        node = TextNode("Text1", TextType.BOLD)
        node2 = TextNode("Text1", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()