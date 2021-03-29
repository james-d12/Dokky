from src.ConfigReader import ConfigReader
from src.DocumentationBuilderTemplate import DocumentationBuilderTemplate
from sys import argv

if __name__ == "__main__":
    if(str(argv[1]) == "--gen"):
        # create default json.
        print("Generating default configuration...")    
    else: 
        cr = ConfigReader(str(argv[1]))
        cr.readConfiguration()

        includeDirectory=cr.getConfig()['includeDirectory']
        outputDirectory = cr.getConfig()['outputDirectory']
        commentDenotion=cr.getConfig()['commentDenotion']
        filterList=cr.getConfig()['filterList']

        writer = DocumentationBuilderTemplate(includeDirectory,commentDenotion,filterList, outputDirectory)
        writer.createDocumentation()