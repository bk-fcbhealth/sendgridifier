import imglist

# Create new HTML file
open("createdfile.html", "w")

# Loop through Image List to get all image locations
imgNames = imglist.images.keys()
for x in imgNames:
    print(x)


