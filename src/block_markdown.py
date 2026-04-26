import textwrap
from enum import Enum

def markdown_to_blocks(markdown):
    clean_md = textwrap.dedent(markdown)
    blocks = []
    for block in clean_md.split('\n\n'):
        if len(block.strip()) == 0:
            continue 

        blocks.append(block.strip())

    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if len(lines) == 1 and lines[0].startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    
    if len(lines) > 2 and lines[0] == '```' and lines[-1] == '```':
        return BlockType.CODE
                
    if all(line.startswith(('>', '> ')) for line in lines):
         return BlockType.QUOTE
    
    if all(line.startswith('- ') for line in lines):
         return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f'{i + 1}. ') for i, line in enumerate(lines)):
         return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
         
        
        
    