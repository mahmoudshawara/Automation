import os
from PIL import Image
logo = input("Enter the name of logo image with extention:")
#create the new folder to save new images with added logo
if not os.path.exists("Imageswithlogo"):
    os.mkdir("Imageswithlogo")
# git width and height of logo
logo_image = Image.open(logo)
logo_width , logo_height = logo_image.size
for filename in os.listdir('.'):
    if not filename.endswith((".png","jpeg","jpg")) or filename==logo:
        continue
    img=Image.open(filename)
    width, height = img.size
    print("adding logo to image %s" %(filename))
    img.paste(logo_image,(width-logo_width,height-logo_height))
    img.save(os.path.join("Imageswithlogo",filename))
    #os.remove(filename) # enable if you want to remove the original image
