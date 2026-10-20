#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir) : 
  paths = []
  files = os.listdir(dir)

  for file in files : 
    if re.search('__\w+__', file) : 
      # create local path 
      new_path = os.path.join(file, dir)
      new_path = os.path.abspath(new_path)
      paths.append(new_path)


  return paths

def zip_files (filenames, new_dir) :
  cmd = f"zip -j {new_dir} <{filenames}>"
  cmd.replace("\n", "")
  print("Command to run: ", cmd)
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output)




def copy_to(paths, new_dir) : 
  # first check if the directory exist
  # if not, create it
  if not os.path.exists(new_dir) :
    os.mkdir(new_dir)

  # now, copy all files at each of the paths locations into the new dir 
  for path in paths : 
    shutil.copy(path, new_dir)
  pass

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = get_special_paths(args[0])

  if todir : 
    copy_to(paths, todir)

  else : 
    for path in paths : 
      print(path)
  
  if tozip :
    file_names = " "
    file_names = file_names.join(paths)
    print(file_names)
    zip_files(file_names, tozip)

if __name__ == '__main__':
  main()
