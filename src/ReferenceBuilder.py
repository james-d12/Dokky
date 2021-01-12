class ReferenceBuilder:
    def __init__(self, files, dictionary):
        self.files = files
        self.dictionary = dictionary

    def writeHTMLData(self, file):
        file.write("<!DOCTYPE html>\n")
        file.write("<html lang='en'>\n")
        file.write("<head>\n")
        file.write("<meta charset='utf-8'/>\n")
        file.write("<meta name='viewport' content='width=device-width, initial-scale=1'>\n")
        file.write("<script src='javascript/utility.js'></script>\n")
        file.write("<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js'></script>\n")
        file.write("<link rel='stylesheet' href='sheets/dark.css' id='theme'>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<div class='sidebar' id='sidebar-id'>\n")
        file.write("<a>Reference</a>\n")
        file.write("<input onkeypress='search()' id='input-search' type='text' placeholder='search...'>\n")

        
    def writeSideBar(self,file):
        file.write("<ul>\n")
        for fileName, data in  self.dictionary.items():
            if len(data) > 0:
                file.write("<div id='sidebar-entry'>\n")
                file.write("    <label>" + fileName + "</label><input class='toggle-checkbox' type='checkbox'/>\n")
                file.write("    <div>\n")
                for key in data:
                    file.write("        <code class='prettyprint'> <a class='header-link' href='#" + str(fileName) + str(data[key]) + "'>" + str(data[key]) + "</a> </li> </code>\n")
                file.write("    </div>\n")
                file.write("</div>\n")

        file.write("</ul>\n")
        file.write("</div>\n")

    def writeReferences(self,file):
        file.write("<div class='main' id='main-id'>\n")
        file.write("<button onclick='toggleCheckboxes();'>Toggle Checkboxes</button>\n")
        file.write("<button onclick='changeTheme();' id='switch'>Switch Theme</button>\n")
        file.write("<button onclick='toggleSidebar();'>Toggle Sidebar</button>\n")
        for fileName, data in self.dictionary.items():
            if len(data) > 0:
                file.write("    <h2 class='fileHeader'>" + str(fileName) + "</h2>\n")
                file.write("    <ul>\n")
                for key in data:
                    file.write("        <code class='prettyprint'> <h3 id='" + str(fileName) + str(data[key]) + "' class='declaration'>" + str(data[key]) + "</h3> </code>\n")
                    file.write("        <li><p>" + str(key) + "</p></li>\n")
                file.write("    </ul>\n")
        file.write("</div>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    def createReference(self, fileName="reference.html"):
        print("Creating reference.html file....")
        with open("docs/"+fileName,'w') as file:
            self.writeHTMLData(file)
            self.writeSideBar(file)
            self.writeReferences(file)