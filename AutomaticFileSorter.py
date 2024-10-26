import os
import shutil

#Set the path for the directory to clean up
path = r"<insert file path you wish to clean up here...>"

#List all files in the specified directory
file_names = os.listdir(path)

#Define the mapping of file types to folder names
folder_map = {
    '.csv': 'csv files',
    '.pbix': 'powerbi files',
    '.xls': 'excel files',
    'reindeer': 'christmas',
    'santa': 'christmas'
}

#Create subfolders if they don't exist
for folder_name in set(folder_map.values()):
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

#Move files to their corresponding folders
for file in file_names:
    source_file = os.path.join(path, file)
    for keyword, folder_name in folder_map.items():
        folder_path = os.path.join(path, folder_name)
        if (file.endswith(keyword) or keyword in file) and not os.path.exists(os.path.join(folder_path, file)):
            shutil.move(source_file, folder_path)
            break
