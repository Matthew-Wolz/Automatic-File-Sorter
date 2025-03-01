# Automatic File Sorter

This Python script organizes files in a specified directory by moving them into designated subfolders based on their file types and naming conventions. It creates the necessary subfolders if they do not already exist.

## Features
- Automatically creates subfolders for:
  - CSV files
  - Power BI files
  - Excel files
  - Themed folders for specific holidays
- Moves files into their corresponding subfolders based on extensions and keywords in the filenames.

## Technologies Used
- Python
- OS Module
- Shutil Module

## How to Run
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the script directory:
   ```sh
   cd <repository_folder>
   ```
3. Run the script:
   ```sh
   python file_sorter.py
   ```

## Future Enhancements
- Add support for more file types.
- Implement a GUI for easier user interaction.
- Enable real-time monitoring of file changes in the directory.
