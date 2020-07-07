import os
import sys
import re
import msvcrt

delete_extension_list = [
  ".jpg",
  ".jpeg",
  ".png",
  ".bmp",
  ".exe",
  ".txt"
]

regex_pattern = re.compile(r"(.*)(\d{4}).*(1080p|720p).*")

def wait_on_keypress():
  print("Press any key to close")
  msvcrt.getch()

argc = len(sys.argv)
if argc < 2:
  print("No path/filename arguments given.")
  wait_on_keypress()

# copy the arguments passed in and prepare to iterate over these items
working_directory = os.path.realpath(os.curdir)
paths_to_process = sys.argv.copy()
paths_to_process.pop(0)
additional_paths = []
files = []

# iterate over the undetermined items to 
while True:
  for path in paths_to_process:
    print("Path:", path)
    if not os.path.isabs(path):
      path = os.path.join(working_directory, path)
      print("Joined path:", path)

    if os.path.isdir(path):
      additional_paths.extend(os.listdir(path))
      print(path, "is a directory")
    elif os.path.isfile(path):
      files.append(path)
      print(path, "is a file")
    print("-----")
  
  if len(additional_paths) < 1:
    break
  else:
    paths_to_process = additional_paths
    additional_paths = []

# print("files:", len(files))


# current_path = os.path.realpath(os.curdir)
# filenames = os.listdir(current_path)

# print("-----")
# for filename in filenames:
#   print("Processing:", filename)
#   original_name, extension = os.path.splitext(filename)
#   original_path = os.path.join(current_path, filename)
#   os.chmod(original_path, 0o0777)

#   extension = extension.lower()
#   if extension in delete_extension_list:
#     print("deleting file with unwanted extension:", extension)
#     #os.remove(original_path)
#     continue

#   results = re.match(regex_pattern, original_name.replace(".", " "))
#   title = results.group(1)
#   year = results.group(2)
#   quality = results.group(3)
#   print("Title:\t", title)
#   print("Year:\t", year)
#   print("Quality:", quality)

#   if extension.lower == "srt":
#     print("Subtitle file detected. Prepending \'.English\' to the file extension")
#     extension = ".English" + extension

#   new_filename = title + "[" + year + "]" + " " + quality + extension
#   new_path = os.path.join(current_path, new_filename)

#   print("Renaming: ", original_path, "\nTo:", new_path)
#   #os.rename(original_path, new_path)
  
#   print("-----")

wait_on_keypress()