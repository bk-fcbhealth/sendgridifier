# Importing the image names from the image list
import imglist
# Duplicating folders
import shutil

# Create new HTML file
# open("createdfile.html", "w")


# Duplicate index.html
shutil.copy('index.html', "sendgrid-index.html")


# Loop through Image List to get all image locations
imgNames = imglist.images.keys()
for x in imgNames:
    print(x)


