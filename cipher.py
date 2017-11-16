from os import listdir, rename
from os.path import isfile, join

#A leading slash in a path means an absolute path, 
# or a path that starts at the root of your filesystem. 
# No leading slash makes the path relative to your working directory (typically wherever you launched the script from).
mypat = r"/Users/dev02/Desktop/Learning/Python/udapythonfound/prank"

def rename_files(mypath):
  #get files from a folder
  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  #print files
  print(onlyfiles);

  #Rename files
  renamed_files = [ rename(join(mypath,f), join(mypath,f.translate(None,"0123456789") )) for f in onlyfiles ]
  

  print("Renamed files")
  print(renamed_files);

rename_files(mypat);
