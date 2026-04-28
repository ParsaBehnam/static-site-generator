import unittest
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq(self):
        node = split_nodes_delimiter([TextNode("This is a **bold** test!", TextType.TEXT)], '**', TextType.BOLD)
        node2 = [TextNode("This is a ", TextType.TEXT),
                 TextNode('bold', TextType.BOLD),
                 TextNode(' test!', TextType.TEXT)]
        self.assertEqual(node, node2)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )