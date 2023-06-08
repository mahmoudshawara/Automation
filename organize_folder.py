import os
import shutil
current_folder = os.path.dirname(os.path.realpath(__file__))
#print(current_folder) 
for filename in os.listdir(current_folder):
    #print(filename)
    #organizr photos in images folder
    if filename.endswith((".png" , ".jpg" , ".jpeg" , ".gif" )):
        if not os.path.exists("Images"):
            #create Images folder if not exists
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print ("Images done")
    #organizr Docs in Documents folder
    if filename.endswith((".doc" , ".docx" , ".pdf" )):
        if not os.path.exists("Documents"):
            #create Documents folder if not exists
            os.mkdir('Documents')
        shutil.copy(filename,"Documents")
        os.remove(filename)
        print ("Documents done")
    #organizr Videos in Videos folder
    if filename.endswith((".mp4" , ".wemb" , ".mkv" )):
        if not os.path.exists("Videos"):
            #create Videos folder if not exists
            os.mkdir('Videos')
        shutil.copy(filename,"Videos")
        os.remove(filename)
        print ("Videos done")
    #organizr Audio in Audio folder
    if filename.endswith((".mp3" , ".wave"  )):
        if not os.path.exists("Audio"):
            #create Audio folder if not exists
            os.mkdir('Audio')
        shutil.copy(filename,"Audio")
        os.remove(filename)
        print ("Audio done")
    #organizr apps in Applications folder
    if filename.endswith((".exe" )):
        if not os.path.exists("Applications"):
            #create Applications folder if not exists
            os.mkdir('Applications')
        shutil.copy(filename,"Applications")
        os.remove(filename)
        print ("Applications done")
    #organizr Archived folders in Archives folder
    if filename.endswith((".exe" )):
        if not os.path.exists("Archives"):
            #create Archives folder if not exists
            os.mkdir('Archives')
        shutil.copy(filename,"Archives")
        os.remove(filename)
        print ("Archives done")