import unittest
from src.inline_markdown import text_to_textnode
from src.textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
     def test_text_to_textnode(self):
        node = [TextNode("this is ", TextType.TEXT), TextNode('bold', TextType.BOLD), TextNode(' and ', TextType.TEXT),
                TextNode('italic', TextType.ITALIC)]
        node2 = text_to_textnode('this is **bold** and _italic_')

        self.assertEqual(node, node2)