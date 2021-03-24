from src.Utility import getFilesFromDirectory, addFilesToDictionary, readFiles
from src.ReferenceBuilder import ReferenceBuilder

class DocumentationBuilder:
    def __init__(self, directory, commentDenotion, filterList):
        self.directory = directory
        self.commentDenotion = commentDenotion
        self.filterList = filterList

    def createReference(self):
        dictionary={}
        files = getFilesFromDirectory(self.directory, self.filterList)
        addFilesToDictionary(files,dictionary)
        readFiles(files, self.commentDenotion, dictionary)
        ReferenceBuilder(files,dictionary).createReference()

    def createDocumentation(self):
        print("Generating documentation.....")
        self.createReference()

        with open("docs/index.html",'w') as file:
            print("Creating index.html file....")
            file.write("<!DOCTYPE html>\n")
            file.write("<html lang='en'>\n") 
            file.write("<head>\n")
            file.write("<meta charset='utf-8'/>\n")
            file.write("<meta name='viewport' content='width=device-width, initial-scale=1'>\n")
            file.write("<script src='javascript/utility.js'></script>\n")
            file.write("<link rel='stylesheet' href='sheets/light.css' id='theme'>\n")
            file.write("</head>\n")
            file.write("<body>\n")
            file.write("<h1> Reference </h1>\n")
            file.write("<a href='reference.html'>Reference</a>\n")
            file.write("</body>\n")
            
        print("Documentation Generated.")
