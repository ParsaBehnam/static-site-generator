from copystatic import copy_static

static_dir = './static'
public_dir = './public'

def main():
   copy_static(static_dir, public_dir) 

main()