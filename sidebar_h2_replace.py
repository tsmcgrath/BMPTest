# python script to list the contents of sidebars on static html pages
import os
# The top argument for the directory walk
topdir = '.'

# The extension to search for
exten = '.html'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # print(os.path.join(dirpath, name))
            file_path = os.path.join(dirpath, name)
            with open(file_path, "r") as f:
                lines = f.readlines()
            with open("yourfile.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != "<h2>State Information</h2>":
                        f.write(line)
