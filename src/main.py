from src.copystatic import copy_static
from src.gen_content import generate_page

static_dir = './static'
public_dir = './public'

def main():
   copy_static(static_dir, public_dir) 
   generate_page('./content/index.md', './template.html', './public/index.html')

main()