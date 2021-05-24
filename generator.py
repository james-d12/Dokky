from src.ConfigReader import ConfigReader
from src.DocumentationBuilderTemplate import DocumentationBuilderTemplate

from sys import argv
from pathlib import Path

def main(generateDefault=False):
    if(generateDefault):
        print("Generating default configuration...")
    else:
        cr = ConfigReader(str(argv[1]))
        cr.readConfiguration()
        cr.printConfiguration()

        includeDirectory=cr.getConfig()['includeDirectory']
        outputDirectory = cr.getConfig()['outputDirectory']
        commentDenotion=cr.getConfig()['commentDenotion']
        filterList=cr.getConfig()['filterList']
        language=cr.getConfig()['language']

        writer = DocumentationBuilderTemplate(language, includeDirectory,commentDenotion,filterList, outputDirectory)
        writer.createDocumentation()
 
if __name__ == "__main__":
    generateDefault = False

    if(len(argv) <= 1):
        print("Invalid Amount of Arguments Given!")
        exit(1)

    if(str(argv[1]) == "--gen"):
         generateDefault = True
    else: 
        file = Path(str(argv[1]))
        if not file.exists():
            print("Given configuration file does not exist. Using defaults!")
            generateDefault = True 

    main(generateDefault)