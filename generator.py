from src.DocumentationBuilder import DocumentationBuilder
from sys import argv

if __name__ == "__main__":
    directory=str(argv[1])
    commentDenotion=str(argv[2])
    filterList=str(argv[3]).replace(" ", "").split(",")

    writer = DocumentationBuilder(directory,commentDenotion,filterList)
    writer.createDocumentation()