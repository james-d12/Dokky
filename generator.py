import os
import sys

dict_data={}

def get_files_from_directory(dirName):
    files = []
    with os.scandir(dirName) as dirs:
        for entry in dirs:
            if(entry.is_dir()):
                files += (get_files_from_directory(entry.path))
            else:
                files.append(entry)
                dict_data[entry.name] = {}
    return files

def read_file(file, commentDenotion):
    comment=""
    addDictEntry = False
    with open(file.path, 'r') as f:
        for line in f:
            line = line.strip()
            if addDictEntry == True:
                dict_data[file.name][comment] = line
                addDictEntry = False
            if line.startswith(commentDenotion):
                line = line.replace(commentDenotion,"")
                addDictEntry = True
                comment=line

def read_files(files, commentDenotion):
    for f in files:
        print("Reading file:", f.name, "....")
        read_file(f, commentDenotion)

def create_html_file(dictionary):
    with open("index.html",'w') as file:
        file.write("<!DOCTYPE html>\n <html lang='en'>\n <head>\n <meta charset='utf-8'/>\n")
        file.write("<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js'></script>\n")
        file.write("<link rel='stylesheet' type='text/css' href='sidebar.css'> <link rel='stylesheet' type='text/css' href='style.css'> </head>\n <body>")
        file.write("<div class='sidebar'>\n <a class='header'>Reference</a>\n")
        
        for fileName, data in dictionary.items():
            if len(data) > 0:
                file.write("<ul>\n <a href='#" + fileName + "' style='font-size: 12px; padding: 0%;'>" + fileName + "</a>\n </ul>\n")
            else:
                next
        file.write("</div>\n")


        file.write("<div class='main'>\n")
        for fileName, data in dictionary.items():
            if len(data) > 0:
                file.write("<h2 class='fileHeader'>" + str(fileName) + "</h2>\n<ul>\n")
                for key in data:
                    file.write("<h3 id='" + fileName + "' class='declaration'>" + str(data[key]) + "</h3>\n")
                    file.write("<li><p>" + str(key) + "</p></li>\n")
                file.write("</ul>\n")
            else:
                next
        file.write("</div>\n</body>\n</html>")
   
acceptedCommentDenotions = ["#", "//"]

directory=str(sys.argv[1])
commentDenotion=str(sys.argv[2])
            
read_files(get_files_from_directory(directory), commentDenotion)
create_html_file(dict_data)




