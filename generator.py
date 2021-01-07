import os
import sys

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

def processFile(file,f, commentDenotion,dictionary):
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
        print("Reading file:", f.name, "....")
        with open(f.path, 'r') as file:
            processFile(f,file,commentDenotion,dictionary)

class ReferenceWriter:
    def __init__(self, files, dictionary):
        self.htmlData = [
            "<!DOCTYPE html>\n",
            "<html lang='en'>\n"
            "<head>\n",
            "<meta charset='utf-8'/>\n",
            "<meta name='viewport' content='width=device-width, initial-scale=1'>\n",
            "<script src='javascript/utility.js'></script>\n",
            "<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js'></script>\n",
            "<link rel='stylesheet' href='sheets/dark.css' id='theme'>\n",
            "</head>\n",
            "<body>\n",
            "<div class='sidebar' id='sidebar-id'>\n",
            "<a>Reference</a>\n",
            "<input onkeypress='search()' id='input-search' type='text' placeholder='search...'>\n",
            "<ul>\n"
        ]
        self.files = files
        self.dictionary = dictionary

    def writeHTMLData(self, file):
        for d in self.htmlData:
            file.write(d)
        
    def writeSideBar(self,file):
        for fileName, data in  self.dictionary.items():
            if len(data) > 0:
                file.write("<div id='sidebar-entry'>\n")
                file.write("    <label>" + fileName + "</label><input class='toggle-checkbox' type='checkbox'/>\n")
                file.write("    <div>\n")
                for key in data:
                    file.write("        <code class='prettyprint'> <a class='header-link' href='#" + str(fileName) + str(data[key]) + "'>" + str(data[key]) + "</a> </li> </code>\n")
                file.write("    </div>\n")
                file.write("</div>\n")

        file.write("</ul>\n")
        file.write("</div>\n")

    def writeReferences(self,file):
        file.write("<div class='main' id='main-id'>\n")
        file.write("<button onclick='toggleCheckboxes();'>Toggle Checkboxes</button>\n")
        file.write("<button onclick='changeTheme();' id='switch'>Switch Theme</button>\n")
        file.write("<button onclick='toggleSidebar();'>Toggle Sidebar</button>\n")
        for fileName, data in self.dictionary.items():
            if len(data) > 0:
                file.write("    <h2 class='fileHeader'>" + str(fileName) + "</h2>\n")
                file.write("    <ul>\n")
                for key in data:
                    file.write("        <code class='prettyprint'> <h3 id='" + str(fileName) + str(data[key]) + "' class='declaration'>" + str(data[key]) + "</h3> </code>\n")
                    file.write("        <li><p>" + str(key) + "</p></li>\n")
                file.write("    </ul>\n")
        file.write("</div>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    def createReference(self, fileName="reference.html"):
        print("Creating index.html file....")
        with open("docs/"+fileName,'w') as file:
            self.writeHTMLData(file)
            self.writeSideBar(file)
            self.writeReferences(file)

class DocumentationWriter:
    def __init__(self, directory, commentDenotion, filterList):
        self.directory = directory
        self.commentDenotion = commentDenotion
        self.filterList = filterList

    def createReference(self):
        dictionary={}
        files = getFilesFromDirectory(self.directory, self.filterList)
        addFilesToDictionary(files,dictionary)
        readFiles(files, self.commentDenotion, dictionary)
        ReferenceWriter(files,dictionary).createReference()

    def createDocumentation(self):
        print("Generating documentation.....")
        self.createReference()

        with open("docs/index.html",'w') as file:
            file.write("<!DOCTYPE html>\n")
            file.write("<html lang='en'>\n") 
            file.write("<head>\n")
            file.write("<meta charset='utf-8'/>\n")
            file.write("<meta name='viewport' content='width=device-width, initial-scale=1'>\n")
            file.write("<script src='javascript/utility.js'></script>\n")
            file.write("<link rel='stylesheet' href='sheets/main.css'>\n")
            file.write("<link rel='stylesheet' href='sheets/dark.css' id='theme'>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<a href='reference.html'>Reference</a>\n")
            file.write("</body>\n")

        print("Documentation Generated.")


def main():
    directory=str(sys.argv[1])
    commentDenotion=str(sys.argv[2])
    filterList=str(sys.argv[3]).replace(" ", "").split(",")

    writer = DocumentationWriter(directory,commentDenotion,filterList)
    writer.createDocumentation()

if __name__ == "__main__":
    main()