import os
import shutil
from src.Readers.Reader import Reader 
from src.Readers.SpecialCharacters import specialCaseCharacters

class PythonReader(Reader): 
    __commentDenotion = "#"

    def __init__(self, directory, filterList):
        super().__init__(directory, filterList)

    def formatLine(self, line):
        line = line.replace(self.__commentDenotion,"")
        for key in specialCaseCharacters: 
            line = line.replace(key, specialCaseCharacters[key])
        return line

    def processFile(self,file, f):
        comment=""
        addDictEntry = False
        for line in f:
            line = line.strip()
            if addDictEntry == True:
                line = formatLine(line)
                self.__dictionary[file.name][comment] = line
                addDictEntry = False
            if line.startswith(self.__commentDenotion):
                line = self.formatLine(line)
                addDictEntry = True
                comment=line

    def readFiles(self):
        for f in self.__files:
            print("Reading file:", f.name, "....")
            with open(f.path, 'r') as file:
                self.processFile(f,file)