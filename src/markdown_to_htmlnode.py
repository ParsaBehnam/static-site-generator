from src.block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from src.htmlnode import HtmlNode, LeafNode, ParentNode
from src.inline_markdown import text_to_textnode
from src.textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_htmlnode(markdown): # converts md document into a HTMLnode containing child nodes
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        child_nodes.append(block_to_html_node(block, block_to_block_type(block)))
    return ParentNode('div', child_nodes)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.HEADING:
            level = 0
            for char in block:
                if char == '#':
                    level += 1
                else:
                    break
            text = block[level + 1:]
            tag = f'h{level}'
            return ParentNode(tag, text_to_children(text))
        
        case BlockType.CODE:
            body = block.removeprefix('```\n').removesuffix('```')
            text_node = TextNode(body, TextType.TEXT)
            leaf_node = text_node_to_html_node(text_node)
            parent_node = ParentNode('code', [leaf_node])
            return ParentNode('pre', [parent_node])
        
        case BlockType.QUOTE:
            splitted = block.split('\n')
            text = list(map(lambda s: s.removeprefix('> '), splitted))
            return ParentNode('blockquote', text_to_children(" ".join(text)))
        
        case BlockType.ORDERED_LIST:
            splitted = block.split('\n')
            text = list(map(lambda s: s.split(". ", 1)[1], splitted))
            nodes_list = []
            for line in text:
                nodes_list.append(ParentNode('li', text_to_children(line)))
            return ParentNode('ol', nodes_list)
           
        case BlockType.UNORDERED_LIST:
            splitted = block.split('\n')
            text = list(map(lambda s: s.split("- ", 1)[1], splitted))
            nodes_list = []
            for line in text:
                nodes_list.append(ParentNode('li', text_to_children(line)))
            return ParentNode('ul', nodes_list)
        
        case BlockType.PARAGRAPH:
            return ParentNode('p', text_to_children(" ".join(block.split('\n'))))

        case _:
            raise ValueError(f"unknown block type: {block_type}")
        
def text_to_children(text):
    nodes_lst = []
    for node in text_to_textnode(text):
        nodes_lst.append(text_node_to_html_node(node))
    
    return nodes_lst