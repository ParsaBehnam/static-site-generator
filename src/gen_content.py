import os
from src.markdown_to_htmlnode import markdown_to_htmlnode
from src.htmlnode import *

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.removeprefix('# ').strip()
        
    raise Exception('no header found')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    for file_name in os.listdir(from_path):
        path = os.path.join(from_path, file_name)
        if os.path.isfile(path):
                new_name = os.path.splitext(file_name)[0] + ".html"
                target_path = os.path.join(dest_path, new_name)

                with open(path) as f:
                    markdown_content = f.read()

                with open(template_path) as f:
                    template_content = f.read()

                html = markdown_to_htmlnode(markdown_content).to_html()
                title = extract_title(markdown_content)
                replaced_template_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html)

                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with open(target_path, 'w') as f:
                    f.write(replaced_template_content)
        else:
            target_path = os.path.join(dest_path, file_name)
            generate_page(path, template_path, target_path)

   



    