import sys
from src.copystatic import copy_static
from src.gen_content import generate_page

static_dir = './static'
docs_dir = './docs'

def main():
   if len(sys.argv) > 1:
      basepath = sys.argv[1]
   else:
      basepath = '/'

   copy_static(static_dir, docs_dir) 
   generate_page('./content/', './template.html', './docs', '/')

main()