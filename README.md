# Overview

Dokky creates a website and code documentation by reading a project's source code for comments. Aims to also be a markdown converter as well.

Creates a reference and home page for all source files in the code.
# Requirements
The only 3rd party python library required is Jinja2. 
- **Jinja2**: https://jinja.palletsprojects.com/en/2.11.x/
    - ```pip install -U jinja2```

# Usage

1. You must comment any functions that you wish to add to be parsed into documentation. Comment denotion can be customised further in the configuration file.
2. Create a configuration file (can be called anything), that follows the following structure:

**Configuration File Structure**
```json
{
    "config": {
        "includeDirectory": ,// The directory of the source code to parse.
        "outputDirectory": ,// The output directory of the documentation.
        "commentDenotion": ,// Specify what is considered a comment.
        "filterList": ,// Specify what file extensions are to be scanned.
        "language": ,// Specify the language of the source code.
        "repository": ,// Specify the GitHub repository of the source code.
    }
}
```

**Example Configuration File Based On Atomic (My Project)**
```json
{
    "config": {
        "includeDirectory": "C:/Dev/C++/Atomic/include",
        "outputDirectory": "./docs",
        "commentDenotion": "//",
        "filterList": [".hpp" ],
        "language": "cpp",
        "repository": "https://github.com/james-d12/Atomic"
    }
}
```

3. Once you've added comments open up a terminal to where 'Dokky.py' is located and run the following command.  
```python ./Dokky.py {config_file_path} ```

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

## Example Home Page

![alt text](https://github.com/james-d12/documentation-generator/blob/master/images/image-01.png?raw=true) 

## Example Source Code Browser (Fixed_Matrix_Engine.hpp from Atomic)

![alt text](https://github.com/james-d12/documentation-generator/blob/master/images/image-02.png?raw=true) 
