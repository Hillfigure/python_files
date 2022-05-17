__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from os.path import join
import shutil

cachepath = os.path.join(os.getcwd(), 'cache')

def clean_cache():
    if os.path.exists(cachepath):
        shutil.rmtree(cachepath)
    os.mkdir(cachepath)

def cache_zip(zip, cache):
    from zipfile import ZipFile
    with ZipFile(zip, 'r') as zipObj:
        zipObj.extractall(cache)

def cached_files():
    return [os.path.abspath(join(cachepath, file)) for file in os.listdir(cachepath)]
 

def find_password(cached= cached_files()):
    for file in cached:
        textfile = open(file, 'r') 
        lines = textfile.readlines()
        for line in lines:
            if line.find("password") != -1:
                return line.split(" ", 1)[1].rstrip('\n')
        textfile.close()

print(find_password())
