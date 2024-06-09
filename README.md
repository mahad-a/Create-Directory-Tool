# Directory and File Structure Creator

This script allows you to create a directory and file structure based on a given input. You can provide the structure as a string for small designs or as a text file for larger ones. The script will parse the structure and create the corresponding directories and files.

## Features

- Create directory and file structures from a string input.
- Create directory and file structures from a text file.
- Automatically handles indentation levels to determine the parent-child relationship between directories and files.

## Usage

### Prerequisites

- Python 3.x installed on your machine.

### Structure Input Formats

#### String Input

You can provide the directory structure directly as a string within the script. This is useful for smaller structures.

#### File Input

You can also provide the directory structure in a text file. This is useful for larger structures. The file should contain the structure in a tree-like format, with indentation representing the directory hierarchy.

### Example Structure

Here is an example of a directory structure in a string format:

media-tracker/
backend/
frontend/
k8s/
.github/
workflows/
ci-cd-pipeline.yml
docker-compose.yml
README.md


And the same structure in a file named `structure.txt`:


### Running the Script

1. **Using String Input**

   Edit the `structure` variable within the script to define your directory structure. Then run the script.

   ```python
   if __name__ == "__main__":
       structure = """
       media-tracker/
           backend/
           frontend/
           k8s/
           .github/
               workflows/
                   ci-cd-pipeline.yml
           docker-compose.yml
           README.md
       """
       create_structure(structure)
    ```
Execute the script:
```bash
python create_structure.py
```
2. **Using File Input**

   Save your directory structure in a file named structure.txt. Ensure the structure_file variable in the script points to this file. Then run the script.
     ```python
    if __name__ == "__main__":
        structure_file = 'structure.txt'
        create_structure_from_file(structure_file)
     ```
  Execute the script:
  
  ```bash
  python create_structure.py
  ```
### Script Explanation
The script consists of two main functions:

#### create_structure(structure, root='.'):

Parses the provided string to create directories and files.
Uses indentation to determine the hierarchy.

#### create_structure_from_file(file_path, root='.'):

Reads the structure from a text file and creates directories and files.
Uses indentation to determine the hierarchy.
The main block of the script allows you to choose between using a string input or a file input to define your directory structure.
