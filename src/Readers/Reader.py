import os 
from abc import ABC, abstractmethod

class Reader:
    def __init__(self, directory, filterList):
        self.__directory = directory
        self.__filterList = filterList
        self.__filesDictionary = {}
        self.__files = []

    def getFilesFromDirectory(self, directory):
        if(directory == None):
            directory = self.__directory

        files = []
        with os.scandir(self.__directory) as dirs:
            for entry in dirs:
                if(entry.is_dir()):
                    files += (getFilesFromDirectory(entry.path))
                else:
                    if len(self.__filterList) >= 1:
                        for f in self.filterList:
                            if f in str(entry):
                                files.append(entry)   
                                break
                    else:
                        files.append(entry)   
        self.__files = files 

    def addFilesToDictionary(self):
        if(len(self.__files) <= 0):
            print("No files present in the reader!.")
            return 

        for f in self.__files:
            self.__dictionary[f.name] = {}

    @abstractmethod
    def formatLine(self, line, commentDenotion):
        pass 

    @abstractmethod
    def processFile(self,file, f, commentDenotion, dictionary):
        pass

    @abstractmethod
    def readFiles(self, files, commentDenotion, dictionary):
        pass 
        