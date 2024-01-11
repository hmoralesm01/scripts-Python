import os
import shutil

path = ""

def organize_files(directory):
    # Get the list of files in the specified directory
    files = os.listdir(directory)

    # Create a dictionary to store file extensions and their corresponding folders
    file_extensions = {}
    
    for file in files:
        # Ignore directories
        if os.path.isdir(file):
            continue
        
        # Get the file extension
        _, extension = os.path.splitext(file)

        # Remove the dot from the extension
        extension = extension[1:]

        # Create a folder for the extension if it doesn't exist
        if extension not in file_extensions:
            os.makedirs(os.path.join(directory, extension), exist_ok=True)
            file_extensions[extension] = os.path.join(directory, extension)

        # Move the file to its corresponding folder
        shutil.move(os.path.join(directory, file), os.path.join(file_extensions[extension], file))

    print("Files organized successfully!")

if __name__ == "__main__":
    # Specify the directory you want to organize
    target_directory = path

    if len(path) == 0:
        print("You did not specify any path")
    else:
        # Call the function to organize files
        organize_files(target_directory)