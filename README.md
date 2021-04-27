# Overview

This is currently being made to assist me in developing Atomic. It automatically parses files and looks for comments in a given style (# //, etc) and then gets the function 
declaration beneath it and creates a home page and a reference page for all the files.

# Requirements

The only 3rd party python library required is Jinja2. It is a python template library used for creating html files.

- Jinja2: https://jinja.palletsprojects.com/en/2.11.x/

# Usage

1. You must comment any functions that you wish to add to the documentation - for languages that use '//' simply put '// {message here}'.
2. Once you've added comments open up a terminal to where 'Generator.py' is located and run the following command.
3. ```python Generator.py docgen.json``` This passes in the default 'docgen.json' configuration file.

# Configuration
Dokky can be configured in the 'docgen.json' file located in the same path as the 'Generator.py' file. It has the following configuration areas: 

- **includeDirectory**: The directory of the source files.
- **outputDirectory**: The directory of the output documentation.
- **commentDenotion**: The denotion for how comments are processed (e.g. what denotes a comment for Dokky to parse)
- **filterList**: A filter list of files with these extensions to parse.
- **language**: The language of the source files.

The default JSON configuration is as follows:

```json
{
    "config": {
        "includeDirectory": "",
        "outputDirectory": "./docs",
        "commentDenotion": "//",
        "filterList": [],
        "language": ""
    }
}
```

# Checklist

## Browsers
- [x] Works on Chrome based.
- [x] Works on Firefox
- [ ] Works on Internet Explorer

## Resolutions
- [x] Works on 1080p Display.
- [ ] Works on Mobile Display
- [ ] Works on 2k Display.
- [ ] Works on 4k Display

# Examples

## Example Reference Page (Empty Directory Given)

![alt text](https://github.com/james-d12/documentation-generator/blob/master/images/image-01.png?raw=true) 

## Example Reference Page (Atomic Directory Given - Triangle.hpp file) 

![alt text](https://github.com/james-d12/documentation-generator/blob/master/images/image-02.png?raw=true) 
