#!/usr/bin/env python

# Makes a string tree of the file directory 
import os 
import sys 

def make_tree(dir_path, indent=0, path_width=2, file_spacing=' ', dir_signal='/*', prefix=''): 
    result = ''
    if len(prefix) > 0: 
        result += prefix[:-path_width] + '_' * path_width + os.path.split(os.path.abspath(dir_path))[-1] + dir_signal + '\n' 
    else: 
        result += prefix + os.path.split(os.path.abspath(dir_path))[-1] + dir_signal + '\n'

    # Get names of each
    dir_contents = os.listdir(dir_path)

    prefix += '|'
    folders = []  
    files = [] 
 
    for content in dir_contents: 
        content_path = os.path.join(dir_path, content) 

        if os.path.isdir(content_path): 
            folders.append(content) 
        else: 
            files.append(content) 

        folders = sorted(folders) 
        files = sorted(files)

    for folder in folders:  
        folder_path = os.path.join(dir_path, folder) 
        result += make_tree(dir_path=folder_path, indent=indent, prefix=prefix+' '*indent) 
             
    for file in files:  
        result += prefix + '_' * path_width + file_spacing + file + '\n'

    return result 

cwd = os.getcwd() 
indent = 2 

result = make_tree(cwd, indent)

print(result) 

