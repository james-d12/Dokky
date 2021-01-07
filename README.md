# Overview

This is currently being made to assist me in developing Atom. It automatically parses files and looks for comments in a given style (# //, etc) and then gets the function 
declaration beneath it and creates a simple html page of each comment within each file.

# Usage

1. You must comment any functions that you wish to add to the documentation - for languages that use '//' simply put '// {message here}'.
2. Once you've added comments open up a terminal to where 'generator.py' is located and run the following command.
3. generator.py {source_file_directory} {comment_type} {filer_list}
4. So for example if i had source files in test/src, and it was written in C++ and wanted to parse any .cpp and .h files, I would do 'generator.py test/src "//" ".cpp, .h"'

