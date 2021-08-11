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


# Loop through Image List to get all image locations
imgNames = imglist.images.keys()
for x in imgNames:
    print(x)
    #for each line in the input file
    for line in originalFile:
        #read replace the string and write to output file
        sendgridFile.write(line.replace(x, "here is the replacement text"))


# close input and output files
originalFile.close()
sendgridFile.close()