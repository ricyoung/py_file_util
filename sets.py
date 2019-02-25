#!/usr/bin/env python

import os
import shutil

#this looks for videos in source folder and places then in sets
#it makes the source folder - then place and MP4 / WMV in that folder
#
fullpath = os.path.join
python_directory = "/source"
start_directory = os.getcwd()
text_files = "/source"

default_path = "./default"

dir_lookup = {
    'mp4': '/.mp4/',
    'wmv': '/.wmv/',
    'mpg': '/.mpg/',
    'mpeg': '/.mpeg/',
    'avi': '/.avi/'
}

def get_extension(filename):
    return filename[filename.rfind('.')+1:]

def main():
    for dirname, dirnames, filenames in os.walk(start_directory):
        for filename in filenames:
            source = fullpath(dirname, filename)
            dirsource = fullpath(dirname)
            dirsource2 = fullpath(dirname) + '/source'
            extension = get_extension(filename)
            print(type(dirsource))
            if dirsource.find('source') == -1:
                if (extension in dir_lookup):
                    #print('found file')
                    if not os.path.exists(dirsource2):
                         os.makedirs(dirsource2)
                    #    os.makedirs(dir_path2)
                    if os.path.exists(dirsource2):
                         x=1
                #     if os.path.exists(dir_path):
                    print()
                    print('dirsource: => ' + dirsource)
                    print('dirsource2: => ' + dirsource2)

                    print('source: ' + source)
                    print('filename: ' + filename)
                    print()
                    shutil.move(source, dirsource2)
                # else:
                #     print('null')
                #    # shutil.move(source, fullpath(default_path, filename))
            else:
                print('already correct')
if __name__ == "__main__":
    main()