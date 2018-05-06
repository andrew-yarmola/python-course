import os
import shutil

def touch(file_name):
    """ Updates file access and modify times or creates file. """
    try :
        os.utime(file_name)
    except :
        open(file_name, 'a').close()

rand_files_dir = 'sorting_dir'
ext = 'ext'

def make_files(path_to_random_text) :
    if not os.path.isdir(rand_files_dir) :
        os.mkdir(rand_files_dir)
    with open(path_to_random_text, 'r') as fp :
        for line in fp :
            basenames = line.split()
            for name in basenames :
                new_file = os.path.join(rand_files_dir,
                                        name + '.' + ext)
                touch(new_file)

def first_letter_sort(sorting_dir) :
    for root, dirs, files in os.walk(sorting_dir) :
        orig_cwd = os.getcwd()
        os.chdir(root)
        for path in files :
            dir_name = path[0].upper()
            # make sure our dir_name is a letter
            if not dir_name.isalpha() : continue
            if not os.path.isdir(dir_name) :
                os.mkdir(dir_name)
            shutil.move(path, dir_name)
        os.chdir(orig_cwd)
        break # only touch files in the top dir
