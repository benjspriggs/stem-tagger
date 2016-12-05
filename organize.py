#!/usr/bin/python3
from yaml import load
# Organize the things

import shutil as shu
import os
import fnmatch

# Return if a filename is "included" according to the settings
def is_included(fn, sett):
  return any(map(lambda incl: incl in fn, sett['include']))

# Get all non-directory filenames in the current directory
def get_filenames(path):
  return [f for f in os.listdir(path) \
    if os.path.isfile(os.path.join(path, f))]

# Organize the files in a directory by a pattern
def load_settings(fn="settings.yml"):
  with open(fn) as f:
    return load(f)

# organize all the files by the unix pattern matching scheme
def organize_tag(unix_pat, destination, sett):
  all_names = get_filenames(os.getcwd())
  names_filter = filter(lambda f: is_included(f, sett), all_names) # filtered list of names, only including the included files
  for match in fnmatch.filter(list(names_filter), unix_pat):
    shu.move(match, destination + "/" + match) # move the file

# make the unix patterns and destination files based
# on a patterns dictionary
def make_patterns(patterns):
  pat = []
  for cat in patterns:
    if cat == 'DEFAULT_ALL':
      for wild in patterns[cat]:
        pat.append(make_wildcard_tuple(wild))
    else:
      pat.append(make_wildcard_tuple(cat))
  return pat

def make_wildcard_tuple(tag):
  return ("*" + tag + "*", os.path.join(os.getcwd(), tag))

if __name__ == "__main__":
  print("Loading settings...")
  sett = load_settings()
  print("Loading patterns...")
  pat_dest = make_patterns(sett['patterns'])
  
  # organize everything
  for (pat, dest) in pat_dest:
    print("Moving '%s' to '%s'..." % (pat, dest))
    # print "Moving files that match %s to %s" % (pat, dest)
    organize_tag(pat, dest, sett)
