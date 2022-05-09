This repo consists of two main python files:\
imgList.py - list of all the images in the directory, pointing to the hosted image URL\
sendgridify.py - main script that replaces the image paths with the hosted URLs\
\
To use:\
-add sendgridify.py and imgList.py to the main directory of your email\
-add image paths and corresponding hosted URLs to the imgList.py file\
-run the script in your project directory by running 'python3 sendgridify.py'\
-script will spit out a new email with the image paths replaced by the hosted URLs\
-new file will be named "sendgrid-index.html"
