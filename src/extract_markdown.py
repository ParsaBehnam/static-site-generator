import re

def extract_markdown_images(text): # ![alt text](https://blahblah.com)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text): # [youtube](https://www.youtube.com/@bootdotdev)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)