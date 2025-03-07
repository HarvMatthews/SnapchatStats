import os
import json
from BasicInfo import Find_Instagram_Dir

def Find_IG_Profile():
        #Get Profile Pictiures/Random image from snapchat
        Images_Dir = Find_Instagram_Dir() + "/media/profile"

        #The folder name can be different per person
        for File in os.listdir(Images_Dir):
                if File.find('.') == -1:
                        Profile_Pic_Dir = Images_Dir + "/" + File
        
        for Image in os.listdir(Profile_Pic_Dir):
                if Image.endswith(".jpg"):
                        #print(Image)
                        Profile_Pic_Dir = Profile_Pic_Dir + "/" + Image
        
        #print(Profile_Pic_Dir)

        return(Profile_Pic_Dir)

#Find_IG_Profile()
