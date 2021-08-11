
# Duplicating folders
import shutil
# Regex for replacement
import re
# For deleting unneeded files after running completes
import os


# Checking if the list of images exists
if os.path.exists("imgList.py"):
    # Importing the image names from the image list
    import imgList  
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

    # Removing configuration files
    if os.path.exists("imgList.pyc"):
        os.remove("imgList.pyc")

        print("finished")
else:
    # Creating the imgList.py file with dummy dictionary
    l = open("imgList.py", "w")
    l.write("images = { <pathname> : <link> }")
    print("please fill out image list in imgList.py")
    print("Use this format:")
    print("images = <pathname_to_image> : <link_to_image>, <pathname_to_image2> : <link_to_image2>")