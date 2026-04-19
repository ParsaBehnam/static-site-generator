import unittest
from htmlnode import HtmlNode

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