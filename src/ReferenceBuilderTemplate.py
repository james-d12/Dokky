import os
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))

class ReferenceBuilderTemplate:
    def __init__(self, files, dictionary, outputDirectory):
        self.files = files
        self.dictionary = dictionary
        self.outputDirectory = "{outputDirectory}/references".format(outputDirectory=outputDirectory)
        self.__createReferenceDirectory()


    def __createReferenceDirectory(self):
        if(os.path.exists(self.outputDirectory) == False):
            try:
                os.mkdir(self.outputDirectory)
            except OSError:
                print ("Creation of the directory %s failed" % self.outputDirectory)
            else:
                print ("Successfully created the directory %s " % self.outputDirectory)


    def createIndex(self, fileNames):
        template = env.get_template('reference_index.html')
        with open("{outputDirectory}/index.html".format(outputDirectory=self.outputDirectory), 'w+') as file:
            template_data = template.render(names=fileNames)
            file.write(template_data)

    def createReferences(self, fileName, fileNames):
        self.createIndex(fileNames)

        print("Creating {fileName}.html file....".format(fileName=fileName))
        template = env.get_template('reference.html')
        with open("{outputDirectory}/{fileName}.html".format(fileName=fileName, outputDirectory=self.outputDirectory), 'w+') as file:
            template_data = template.render(names=fileNames, name=fileName, items=self.dictionary.items())
            file.write(template_data)