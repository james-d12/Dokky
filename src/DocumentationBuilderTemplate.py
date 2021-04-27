from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))

from src.Utility import getFilesFromDirectory, addFilesToDictionary, readFiles, formatLine
from src.ReferenceBuilderTemplate import ReferenceBuilderTemplate
from src.SourceBuilderTemplate import SourceBuilderTemplate

class DocumentationBuilderTemplate:
    def __init__(self, language, directory, commentDenotion, filterList, outputDirectory):
        self.language = language
        self.directory = directory
        self.commentDenotion = commentDenotion
        self.filterList = filterList
        self.outputDirectory = outputDirectory

    def createReferences(self):
        allFiles = getFilesFromDirectory(self.directory, self.filterList)

        fileNames = []
        for f in allFiles:
            fileNames.append(f.name)


        for i in range(0, len(allFiles)):
            dictionary = {}
            files = [allFiles[i]]

            addFilesToDictionary(files, dictionary)
            readFiles(files, self.commentDenotion, dictionary)
            ReferenceBuilderTemplate(dictionary, self.outputDirectory).createReferences(allFiles[i].name, fileNames)

    def createSources(self):
        allFiles = getFilesFromDirectory(self.directory, self.filterList)

        fileNames = []
        for f in allFiles:
            fileNames.append(f.name)

        for i in range(0, len(allFiles)):
            file = allFiles[i]
            with open(file, 'r') as f:
                line = f.read()
                html = formatLine(line, self.commentDenotion)
            SourceBuilderTemplate(self.language, self.outputDirectory).createSources(html, allFiles[i].name, fileNames)

    def createIndex(self):
        template = env.get_template('index.html')
        with open("{outputDirectory}/index.html".format(outputDirectory=self.outputDirectory), 'w+') as file:
            template_data = template.render()
            file.write(template_data)

    def createDocumentation(self):
        print("Generating documentation.....")
        self.createIndex()
        print("Generating References.....")
        self.createReferences()
        print("Generating Sources.....")
        self.createSources()