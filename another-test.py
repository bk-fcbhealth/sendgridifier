# Importing the image names from the image list
import imglist
# Duplicating folders
import shutil

# Create new HTML file
# open("createdfile.html", "w")


# Duplicate index.html
shutil.copy('index.html', "sendgrid-index.html")


#input file
originalFile = open("index.html", "rt")
#output file to write the result to
sendgridFile = open("sendgrid-index.html", "wt")



# def replace_all(


# Loop through Image List to get all image locations
imgNames = imglist.images.keys()

dic = imglist.images
# print(dic)
for line in originalFile:
    # print(line)
    for key, value in dic.items():
        # print(dic.items())
        # print(key, value)
        # print(line)
        print(key)
        newLine = line.replace(key, value)
        # print("newLine: " + newLine)
        sendgridFile.write(newLine)
    

# close input and output files
originalFile.close()
sendgridFile.close()