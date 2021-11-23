import os
import json
import src.Constant as Constant

from src.Utility import createDirectoryIfNotExists

class ConfigReader:
    def __init__(self, filePath):
        self.filePath = filePath 
        self.config = {}

    def validateConfiguration(self):
        createDirectoryIfNotExists(self.config[Constant.INCLUDE_DIRECTORY_KEY])
        createDirectoryIfNotExists(self.config[Constant.OUTPUT_DIRECTORY_KEY])
        createDirectoryIfNotExists(self.config[Constant.OUTPUT_DIRECTORY_KEY] + "/public")
        createDirectoryIfNotExists(self.config[Constant.OUTPUT_DIRECTORY_KEY] + "/sources")
        createDirectoryIfNotExists(self.config[Constant.OUTPUT_DIRECTORY_KEY] + "/references")

    def readConfiguration(self):
        with open(self.filePath, 'r') as file:
            try:
                data = json.load(file)['config']

                self.config[Constant.INCLUDE_DIRECTORY_KEY] = data[Constant.INCLUDE_DIRECTORY_KEY]
                self.config[Constant.OUTPUT_DIRECTORY_KEY] = data[Constant.OUTPUT_DIRECTORY_KEY]
                self.config[Constant.COMMENT_DENOTION_KEY] = data[Constant.COMMENT_DENOTION_KEY]
                self.config[Constant.FILTER_LIST_KEY] = data[Constant.FILTER_LIST_KEY]
                self.config[Constant.LANGUAGE_KEY] = data[Constant.LANGUAGE_KEY]
                self.config[Constant.REPOSITORY_KEY] = data[Constant.REPOSITORY_KEY]

                self.validateConfiguration()
            except Exception as error:
                print("An error occurred reading the configuration file with error: {error}".format(error=error))
                exit(1)
