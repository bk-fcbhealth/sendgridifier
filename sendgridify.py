# Importing the image names from the image list
import imgList
# Duplicating folders
import shutil
# Regex for replacement
import re
# For deleting unneeded files after running completes
import os



# Duplicate index.html
shutil.copy('index.html', "sendgrid-index.html")

# List of images
dic = imgList.images

# Make all replacements
with open('sendgrid-index.html', 'r+') as f:
    text = f.read()
    for key, value in dic.items():
        text = re.sub(key, value, text)
        f.seek(0)
        f.write(text)
        f.truncate()


if os.path.exists("imgList.pyc"):
  os.remove("imgList.pyc")

print("finished")
