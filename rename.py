from pathlib import Path
from os import listdir, rename
from os.path import isfile, join

path = 'AA'

files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()

for f in files:
    f2 = f.replace('wiki_', 'wiki_0')
    rename('AA/' + f, 'AA/' + f2)