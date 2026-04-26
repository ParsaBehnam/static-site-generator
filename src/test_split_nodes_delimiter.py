import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq(self):
        node = split_nodes_delimiter([TextNode("This is a **bold** test!", TextType.TEXT)], '**', TextType.BOLD)
        node2 = [TextNode("This is a ", TextType.TEXT),
                 TextNode('bold', TextType.BOLD),
                 TextNode(' test!', TextType.TEXT)]
        self.assertEqual(node, node2)