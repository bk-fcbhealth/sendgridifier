# Importing the image names from the image list
import imgList
# Duplicating folders
import shutil
# Regex for replacement
import re



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

print("finished")
