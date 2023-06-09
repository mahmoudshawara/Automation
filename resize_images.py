import os
from PIL import Image
fit_size = int(input("Enter the desired size :"))
#creat folder to save resized images an check if it created first
if not os.path.exists("ResizedImages"):
    os.mkdir("ResizedImages")
#print(os.listdir('.'))
for filename in os.listdir('.'):
    if not filename.endswith((".png" , ".jpg" , ".jpeg")):
        continue
    #print(filename)
    image= Image.open(filename)
    width , height = image.size
    if width > fit_size and height > fit_size :
        if width > height:
            width = fit_size
            height = int((fit_size / width)* height)
        else:
            height = fit_size
            width = int((fit_size / height)* width)
        image = image.resize((width,height))
    print ("Resizing ..... %s" %(filename))
    image =image.save(os.path.join("ResizedImages",filename))
    #os.remove(filename) # enable if you want to remove the original image

