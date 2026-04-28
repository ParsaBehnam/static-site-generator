from src.textnode import TextType, TextNode
from src.extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes:
        raise Exception('Empty Text!')
    new_nodes = []
    for old_node in old_nodes:
        splitted_lst = old_node.text.split(delimiter)
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if len(splitted_lst) % 2 == 0:
            raise Exception("invalid delimiter")
        
        current_node = []

        for i, sentence in enumerate(splitted_lst):
            if sentence == "":
                continue
            if i %2 == 0:
                current_node.append(TextNode(sentence, TextType.TEXT))
            else:
                current_node.append(TextNode(sentence, text_type))

        new_nodes.extend(current_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if extract_markdown_images(old_node.text) == []:
            new_nodes.append(old_node)
            continue
        current_node = []
        remaining_text = old_node.text

        for image_alt, image_link in extract_markdown_images(remaining_text):
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0]:
                current_node.append(TextNode(sections[0], TextType.TEXT))
            current_node.append(TextNode(image_alt, TextType.IMAGE, image_link))
            remaining_text = sections[1]
        if remaining_text:
            current_node.append(TextNode(remaining_text, TextType.TEXT))
        new_nodes.extend(current_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if extract_markdown_links(old_node.text) == []:
            new_nodes.append(old_node)
            continue
        current_node = []
        remaining_text = old_node.text

        for text, text_link in extract_markdown_links(remaining_text):
            sections = remaining_text.split(f"[{text}]({text_link})", 1)
            if sections[0]:
                current_node.append(TextNode(sections[0], TextType.TEXT))
            current_node.append(TextNode(text, TextType.LINK, text_link))
            remaining_text = sections[1]
        if remaining_text:
            current_node.append(TextNode(remaining_text, TextType.TEXT))
        new_nodes.extend(current_node)
    return new_nodes
        