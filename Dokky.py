from src.ConfigReader import ConfigReader
from src.Builder import Builder

from sys import argv
from pathlib import Path


def main():
    cr = ConfigReader(str(argv[1]))
    cr.readConfiguration()

    builder = Builder(cr.config)
    builder.build()


if __name__ == "__main__":
    if(len(argv) <= 1):
        print("Invalid Amount of Arguments Given!")
        exit(1)

    file = Path(str(argv[1]))
    if not file.exists():
        print("Provided config file does not exist!")
        exit(1)

    main()
