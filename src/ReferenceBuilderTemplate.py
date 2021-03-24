import os
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))

class ReferenceBuilderTemplate:
    def __init__(self, files, dictionary):
        self.__createReferenceDirectory()
        self.files = files
        self.dictionary = dictionary


    def __createReferenceDirectory(self):
        path = "./docs/references"
        if(os.path.exists(path) == False):
            try:
                os.mkdir(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s " % path)


    def createIndex(self, fileNames):
        template = env.get_template('reference_index.html')
        with open("docs/references/index.html", 'w+') as file:
            template_data = template.render(names=fileNames)
            file.write(template_data)

    def createReferences(self, fileName, fileNames):
        self.createIndex(fileNames)

        print("Creating {fileName}.html file....".format(fileName=fileName))
        template = env.get_template('reference.html')
        with open("docs/references/{fileName}.html".format(fileName=fileName), 'w+') as file:
            template_data = template.render(names=fileNames, name=fileName, items=self.dictionary.items())
            file.write(template_data)