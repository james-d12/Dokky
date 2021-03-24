from src.DocumentationBuilder import DocumentationBuilder
from src.DocumentationBuilderTemplate import DocumentationBuilderTemplate
from sys import argv

if __name__ == "__main__":

    if(str(argv[4]) == "old"):
        print("Running old code...")
        directory=str(argv[1])
        commentDenotion=str(argv[2])
        filterList=str(argv[3]).replace(" ", "").split(",")

        writer = DocumentationBuilder(directory,commentDenotion,filterList)
        writer.createDocumentation()
    else:        
        print("Running new code...")
        directory=str(argv[1])
        commentDenotion=str(argv[2])
        filterList=str(argv[3]).replace(" ", "").split(",")

        writer = DocumentationBuilderTemplate(directory,commentDenotion,filterList)
        writer.createDocumentation()