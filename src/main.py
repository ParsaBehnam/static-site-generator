from textnode import TextType
from textnode import TextNode

def main():
    text_node = TextNode("sample_text", TextType.BOLD, 'www.boot.dev')
    print(text_node)

main()