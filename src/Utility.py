import os
import shutil

def getFilesFromDirectory(dirName, filterList=[]):
    files = []
    with os.scandir(dirName) as dirs:
        for entry in dirs:
            if(entry.is_dir()):
                files += (getFilesFromDirectory(entry.path, filterList))
            else:
                if len(filterList) >= 1:
                    for f in filterList:
                        if f in str(entry):
                            files.append(entry)   
                            break
                else:
                    files.append(entry)   
    return files

def addFilesToDictionary(files,dictionary):
    for f in files:
        dictionary[f.name] = {}

specialCaseCharacters = {
    "<": "&lt", 
    ">": "&gt", 
    #"&": "&amp", 
    #'"': "&quot", 
    #"'": "&apos", 
    #"£": "&pound"
}

def formatLine(line, commentDenotion):
    line = line.replace(commentDenotion,"")
    for key in specialCaseCharacters: 
        line = line.replace(key, specialCaseCharacters[key])
    return line

def processFile(file, f, commentDenotion, dictionary):
    comment=""
    addDictEntry = False
    for line in f:
        line = line.strip()
        if addDictEntry == True:
            line = formatLine(line, commentDenotion)
            dictionary[file.name][comment] = line
            addDictEntry = False
        if line.startswith(commentDenotion):
            line = formatLine(line, commentDenotion)
            addDictEntry = True
            comment=line

def readFiles(files, commentDenotion, dictionary):
    for f in files:
        with open(f.path, 'r') as file:
            processFile(f,file,commentDenotion,dictionary)
    
def getAllSortedFileNames(includeDirectory, filterList):
    allFiles = getFilesFromDirectory(includeDirectory, filterList)

    fileNames = []
    for f in allFiles:
        fileNames.append(f.name)
    return fileNames

def copyAssets(dest):
    src = (os.path.dirname(os.path.realpath(__file__))) + "\Assets\public"
    shutil.copytree(src, dest, dirs_exist_ok=True) 

def createDirectoryIfNotExists(dir):
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except Exception as error:
            print((f"Error occured making directory: {dir} with error: {error}"))