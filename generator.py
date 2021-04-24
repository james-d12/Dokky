from src.ConfigReader import ConfigReader
from src.DocumentationBuilderTemplate import DocumentationBuilderTemplate
from src.Readers.PythonReader import PythonReader

from sys import argv
from pathlib import Path

def main(generateDefault=False):
    if(generateDefault):
        print("Generating default configuration...")
    else:
        cr = ConfigReader(str(argv[1]))
        cr.readConfiguration()

        includeDirectory=cr.getConfig()['includeDirectory']
        outputDirectory = cr.getConfig()['outputDirectory']
        commentDenotion=cr.getConfig()['commentDenotion']
        filterList=cr.getConfig()['filterList']
        language=cr.getConfig()['language']

        writer = DocumentationBuilderTemplate(includeDirectory,commentDenotion,filterList, outputDirectory)
        writer.createDocumentation()

if __name__ == "__main__":
    generateDefault = False
    if(str(argv[1]) == "--gen"):
         generateDefault = True
    else: 
        file = Path(str(argv[1]))
        if not file.exists():
            print("Given configuration file does not exist. Using defaults!")
            generateDefault = True 

    main(generateDefault)