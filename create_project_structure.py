import os

def create_structure(structure, root='.'):
    lines = structure.strip().split('\n')
    stack = []
    current_indent = -1

    for line in lines:
        indent = len(line) - len(line.lstrip())
        name = line.strip()
        
        # Determine if it's a directory or a file
        is_directory = not any(ext in name for ext in ('.',))
        
        # Adjust stack according to the current indentation
        while indent <= current_indent:
            stack.pop()
            current_indent -= 4
        
        # Determine the current path
        current_path = os.path.join(root, *stack)
        target_path = os.path.join(current_path, name)

        if is_directory:
            os.makedirs(target_path, exist_ok=True)
            stack.append(name)
            current_indent = indent
        else:
            os.makedirs(current_path, exist_ok=True)
            with open(target_path, 'w') as f:
                pass  # Create an empty file

def create_structure_from_file(file_path, root='.'):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    stack = []
    current_indent = -1

    for line in lines:
        indent = len(line) - len(line.lstrip())
        name = line.strip()
        
        # Determine if it's a directory or a file
        is_directory = not any(ext in name for ext in ('.',))
        
        # Adjust stack according to the current indentation
        while indent <= current_indent:
            stack.pop()
            current_indent -= 4
        
        # Determine the current path
        current_path = os.path.join(root, *stack)
        target_path = os.path.join(current_path, name)

        if is_directory:
            os.makedirs(target_path, exist_ok=True)
            stack.append(name)
            current_indent = indent
        else:
            os.makedirs(current_path, exist_ok=True)
            with open(target_path, 'w') as f:
                pass  # Create an empty file

if __name__ == "__main__":
    # Specify the root directory and the structure
    root = r"D:\PersonalProjects\file_tool\Unknown"
    
    # Example structure as a string
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
    
    # If you want to read from a file instead, uncomment the following lines:
    # structure_file = 'structure.txt'
    # create_structure_from_file(structure_file, root=root)
    
    # Create the structure
    create_structure(structure) # creates the structure in the current folder
    create_structure(structure, root=root) # creates the structure in a defined 