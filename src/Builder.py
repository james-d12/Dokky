import src.Utility as Utility
import src.Constant as Constant

class Builder:
    def __init__(self, config):
        self.config = config
        self.allFiles = Utility.getFilesFromDirectory(config[Constant.INCLUDE_DIRECTORY_KEY], config[Constant.FILTER_LIST_KEY])
        self.fileNames = sorted([f.name for f in self.allFiles])

    def build(self):
        self.copyAssets()
        self.buildIndexFile()
        self.buildSourceIndexFile()
        self.buildReferenceIndexFile()

        for file in self.allFiles:
            dictionary = {}
            files = [file]

            Utility.addFilesToDictionary(files, dictionary)
            Utility.readFiles(files, self.config[Constant.COMMENT_DENOTION_KEY], dictionary)

            self.buildReferenceFiles(file.name, dictionary)
            with open(file, 'r') as f:
                html = Utility.formatLine(f.read(), self.config[Constant.COMMENT_DENOTION_KEY])
                self.buildSourceFiles(file.name, html)

    def copyAssets(self):
        Utility.copyAssets(
            self.config[Constant.OUTPUT_DIRECTORY_KEY] + "/public")

    def buildIndexFile(self):
        template = Constant.JINJA2_ENV.get_template('Index.html')
        with open(f"{self.config[Constant.OUTPUT_DIRECTORY_KEY]}/Index.html", 'w+') as file:
            template_data = template.render(
                repository=self.config[Constant.REPOSITORY_KEY])
            file.write(template_data)

    def buildSourceIndexFile(self):
        template = Constant.JINJA2_ENV.get_template('SourceIndex.html')
        with open(f"{self.config[Constant.OUTPUT_DIRECTORY_KEY]}/sources/Index.html", 'w+') as file:
            template_data = template.render(names=self.fileNames)
            file.write(template_data)

    def buildReferenceIndexFile(self):
        template = Constant.JINJA2_ENV.get_template('ReferenceIndex.html')
        with open(f"{self.config[Constant.OUTPUT_DIRECTORY_KEY]}/references/Index.html", 'w+') as file:
            template_data = template.render(names=self.fileNames)
            file.write(template_data)

    def buildSourceFiles(self, fileName, html):
        template = Constant.JINJA2_ENV.get_template('Source.html')
        with open(f"{self.config[Constant.OUTPUT_DIRECTORY_KEY]}/sources/{fileName}.html", 'w+') as file:
            template_data = template.render(
                names=self.fileNames, name=fileName, html=html, language=self.config[Constant.LANGUAGE_KEY])
            file.write(template_data)

    def buildReferenceFiles(self, fileName, dictionary):
        template = Constant.JINJA2_ENV.get_template('Reference.html')
        with open(f"{self.config[Constant.OUTPUT_DIRECTORY_KEY]}/references/{fileName}.html", 'w+') as file:
            template_data = template.render(
                names=self.fileNames, name=fileName, items=dictionary.items())
            file.write(template_data)