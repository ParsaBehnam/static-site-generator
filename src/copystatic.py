from os import path, mkdir, listdir
from shutil import rmtree, copy

def copy_static(src_dir, target_dir):
    if not path.exists(src_dir):
        raise Exception('invalid source directory')

    if path.exists(target_dir):
        rmtree(target_dir, ignore_errors= False, onexc= None)
        
    mkdir(target_dir)

    for file_name in listdir(src_dir):
        src_path = path.join(src_dir, file_name)
        target_path = path.join(target_dir, file_name)

        if path.isfile(src_path):
            copy(src_path, target_path)
            print(f'{file_name} copied from {src_dir} to {target_dir}')
        else:
            copy_static(src_path, target_path)
    

    