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
  ".txt",
  ".dat"
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

# iterate over the undetermined items (BFS)
while True:
  for path in paths_to_process:
    print("Path:", path)
    if not os.path.isabs(path):
      path = os.path.abspath(path)
      print("Abs path:", path)

    if os.path.isdir(path):
      print(path, "is a directory")
      for dir_item in os.listdir(path):
        additional_paths.append(os.path.join(path, dir_item))  
    elif os.path.isfile(path):
      files.append(path)
      print(path, "is a file")
    print("-----")
  
  #continue to traverse any newly-discovered directories
  if len(additional_paths) < 1:
    break
  else:
    paths_to_process = additional_paths
    additional_paths = []

print("files found:", len(files))
print("-----")


for file_path in files:
  print("Processing:", file_path)
  os.chmod(file_path, 0o0777)
  original_path, extension = os.path.splitext(file_path)
  parent_path, original_name = os.path.split(original_path)

  print("Extension:", extension)
  extension = extension.lower()
  if extension in delete_extension_list:
    print("deleting file with unwanted extension:", extension)
    os.remove(file_path)
    continue

  regex_match = re.match(regex_pattern, original_name.replace(".", " "))
  if regex_match is None:
    print("unable to match regex pattern to file. Skipping.")
    continue

  title = regex_match.group(1)
  year = regex_match.group(2)
  quality = regex_match.group(3)
  print("Title:\t  ", title)
  print("Year:\t  ", year)
  print("Quality:", quality)

  if extension == ".srt":
    print("Subtitle file detected. Prepending \'.English\' to the file extension")
    extension = ".English" + extension

  new_filename = title + "[" + year + "]" + " " + quality + extension
  new_path = os.path.join(parent_path, new_filename)

  print("Renaming: ", file_path, "\nTo:", new_path)
  os.rename(file_path, new_path)
  
  print("-----")

wait_on_keypress()