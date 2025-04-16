import os

# Define the project structure
project_structure = {
    "resume_analyzer": {
        "app.py": "",
        "static": {
            "css": {"styles.css": "/* Add your CSS here */"},
            "js": {"main.js": "// Add your JavaScript here"},
        },
        "templates": {
            "index.html": "<!-- Main upload page -->",
            "results.html": "<!-- Results display page -->",
        },
        "utils": {
            "__init__.py": "# Initialize utils package",
            "document_parser.py": "# Add document parsing logic here",
            "resume_analyzer.py": "# Add resume analysis logic here",
            "job_matcher.py": "# Add job matching logic here",
            "text_processor.py": "# Add text processing utilities here",
        },
        "requirements.txt": "# List project dependencies here",
        "README.md": "# Project documentation",
    }
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # If it's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursively create sub-structures
        else:  # If it's a file
            with open(path, "w") as file:
                file.write(content)

# Create the project structure
base_path = os.getcwd()  # Current working directory
create_structure(base_path, project_structure)
print(f"Project structure created at {base_path}/resume_analyzer")
