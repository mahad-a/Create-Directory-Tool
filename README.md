# Directory and File Structure Creator

This application allows you to create a directory and file structure based on a given input through a graphical user interface (GUI). You can provide the structure as a string for small designs or as a text file for larger ones. The application will parse the structure and create the corresponding directories and files.

## Features

- Create directory and file structures from a string input via the GUI.
- Create directory and file structures from a text file via the GUI.
- Automatically handles indentation levels to determine the parent-child relationship between directories and files.

## Usage

### Prerequisites

- Python 3.x installed on your machine.
- PyQt5 library installed:
```sh
pip install PyQt5
```

## Running the Application

1. Starting the GUI
To start the application, run the executable `create-directory-tool.exe`. Or from an ide, run the main.py script. This will launch the graphical user interface where you can select the root folder, input the directory structure as a string, or upload a text file with the structure. 

```bash
python main.py
```

2. Using the GUI
- Select the Root Folder
- Input as String or Upload a Text File

## Example Structure
### String Input

```bash
media-tracker/
   backend/
   frontend/
   k8s/
   .github/
   workflows/
      ci-cd-pipeline.yml
      docker-compose.yml
   README.md
```

## Script Explanation
While the primary use of the application is through the GUI, the backend consists of two main functions:

`create_structure(structure, root='.')`
Parses the provided string to create directories and files. Uses indentation to determine the hierarchy.

`create_structure_from_file(file_path, root='.')`
Reads the structure from a text file and creates directories and files. Uses indentation to determine the hierarchy.