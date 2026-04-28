import unittest
from src.htmlnode import HtmlNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_no_input(self):
        node = HtmlNode()
        node2 = HtmlNode()
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = HtmlNode('<p>', 'some_text',["h1"])
        node2 = HtmlNode('<img>', 'some_other_text',["a"], {"src": "url"})
        self.assertNotEqual(node, node2)

    def test_eq_propsToHtml(self):
        aprops = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        
        string = ' href="https://www.google.com" target="_blank"'
        node = HtmlNode('<a>', 'click here!', None, aprops)
        result = node.props_to_html()
        self.assertEqual(string, result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click, here", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">click, here</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    if __name__ == "__main__":
        unittest.main()