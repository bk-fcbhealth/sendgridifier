# Importing the image names from the image list
import imglist
# Duplicating folders
import shutil

import re

# Create new HTML file
# open("createdfile.html", "w")


# Duplicate index.html
shutil.copy('index.html', "sendgrid-index.html")


with open('sendgrid-index.html', 'r+') as f:
    text = f.read()
    print(text)
    text = re.sub('head', 'HEAD', text)
    f.seek(0)
    f.write(text)
    f.truncate()



# def replace_all(


# # Loop through Image List to get all image locations
# imgNames = imglist.images.keys()

# dic = imglist.images
# # print(dic)
# for line in originalFile:
#     # print(line)
#     for key, value in dic.items():
#         # print(dic.items())
#         # print(key, value)
#         # print(line)
#         print(key)
#         newLine = line.replace(key, value)
#         # print("newLine: " + newLine)
#         sendgridFile.write(newLine)
    

# # close input and output files
# originalFile.close()
# sendgridFile.close()