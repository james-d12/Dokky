from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))


class ReferenceBuilderTemplate:
    def __init__(self, files, dictionary):
        self.files = files
        self.dictionary = dictionary

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