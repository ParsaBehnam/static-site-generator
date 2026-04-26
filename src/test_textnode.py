import unittest
from textnode import TextType, TextNode, text_node_to_html_node
from inline_markdown import text_to_textnode

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()