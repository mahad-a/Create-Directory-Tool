import os

def create_structure(structure, root='.'):
    # grab the passed string structure and prepare to build project
    lines = structure.strip().split('\n')
    stack = []
    current_indent = 0

    for line in lines: # for each line in the string (each file or directory)
        indent = len(line) - len(line.lstrip())
        name = line.strip()
        
        # adjust stack according to the current indentation
        while stack and indent <= stack[-1][1]:
            stack.pop()
        
        # determine the current path 
        current_path = os.path.join(root, *[d[0] for d in stack])
        target_path = os.path.join(current_path, name)

        # determine if it's a directory or a file
        if '.' not in name:
            os.makedirs(target_path, exist_ok=True)
            stack.append((name, indent))
        else:
            os.makedirs(current_path, exist_ok=True)
            with open(target_path, 'w') as f:
                pass  # create an empty file

# same as create_structure function, except takes a textfile as input rather than string
def create_structure_from_file(file_path, root='.'):
    with open(file_path, 'r') as file: # parse the passed textfile
        lines = file.readlines()
    
    stack = []
    current_indent = 0

    for line in lines: # for each line in the textfile
        indent = len(line) - len(line.lstrip())
        name = line.strip()
        
        # adjust stack according to the current indentation
        while stack and indent <= stack[-1][1]:
            stack.pop()
        
        # determine the current path
        current_path = os.path.join(root, *[d[0] for d in stack])
        target_path = os.path.join(current_path, name)

        # determine if it's a directory or a file
        if '.' not in name:
            os.makedirs(target_path, exist_ok=True)
            stack.append((name, indent))
        else:
            os.makedirs(current_path, exist_ok=True)
            with open(target_path, 'w') as f:
                pass  # create an empty file
