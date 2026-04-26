from textnode import TextType, TextNode

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
            if i %2 == 0:
                current_node.append(TextNode(sentence, TextType.TEXT))
            else:
                current_node.append(TextNode(sentence, text_type))

        new_nodes.extend(current_node)
    return new_nodes
        