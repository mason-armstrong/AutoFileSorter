import os
import shutil
from pathlib import Path



#Function that sorts files in a folder
def sort_files_in_folder(mypath): 

    files = os.listdir(mypath)

    #Folder Making
    for file in files: 
        name, ext = os.path.splitext(file)

        #Loops through folder and stores extensions in list
        ext = ext[1:]
        if ext == '':
            continue

        #If folder exists, move file to folder    
        if os.path.exists(mypath+ '\\'+ext):
            shutil.move(mypath + '\\' + file, mypath + '\\' + ext + '\\' + file)
      
        #Creates new directory if none exists
        else:
            os.makedirs(mypath+'\\'+ext)
            shutil.move(mypath + '\\' + file, mypath + '\\' + ext + '\\' + file)

if __name__ == "__main__":

    #Get User Download Folder
    downloadFolderPath = str(os.path.join(Path.home(), "Downloads"))
    print("Files sorted in: " + downloadFolderPath)

    #Pass User Download File Into Sort Function
    sort_files_in_folder(downloadFolderPath)
  