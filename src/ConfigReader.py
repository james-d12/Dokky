import os
import json

class ConfigReader:

    def __init__(self, filePath):
        self.filePath = filePath 
        self.config = {}

    def readConfiguration(self):
        with open(self.filePath, 'r') as file:
            try:
                data = json.load(file)['config']
                if(os.path.exists(data['includeDirectory']) == False):
                    print("Directory does not exist!")
                    exit(1)
                else: 
                    self.config = data 
            except:
                print("An exception occurred, exiting program!")
                exit(1)

    def printConfiguration(self):
        print(self.config)

        print("Configuration")
        print("-----------------------------")
        print("     Include Directory: ", self.config['includeDirectory'])
        print("     Output Directory: ", self.config['outputDirectory'])
        print("     Comment Denotion: ", self.config['commentDenotion'])
        print("     Filter List: ", self.config['filterList'])

    def getConfig(self):
        return self.config 