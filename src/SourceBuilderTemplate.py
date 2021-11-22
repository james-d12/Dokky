import os
from src.Constant import JINJA2_ENV as env

class SourceBuilderTemplate:
    def __init__(self, language, outputDirectory):
        self.language = language
        self.outputDirectory = "{outputDirectory}/sources".format(outputDirectory=outputDirectory)
        self.__createSourceDirectory()

    def __createSourceDirectory(self):
        if(os.path.exists(self.outputDirectory) == False):
            try:
                os.mkdir(self.outputDirectory)
            except OSError:
                print ("Creation of the directory %s failed" % self.outputDirectory)
            else:
                print ("Successfully created the directory %s " % self.outputDirectory)

    def createIndex(self, fileNames):
        template = env.get_template('source_index.html')
        with open("{outputDirectory}/index.html".format(outputDirectory=self.outputDirectory), 'w+') as file:
            template_data = template.render(names=fileNames)
            file.write(template_data)

    def createSources(self, html, fileName, fileNames):
        fileNames = sorted(fileNames)
        self.createIndex(fileNames)

        print("Creating {outputDirectory}/{fileName}.html file....".format(outputDirectory=self.outputDirectory, fileName=fileName))
        template = env.get_template('source.html')
        with open("{outputDirectory}/{fileName}.html".format(fileName=fileName, outputDirectory=self.outputDirectory), 'w+') as file:
            template_data = template.render(names=fileNames, name=fileName, html=html, language=self.language)
            file.write(template_data)