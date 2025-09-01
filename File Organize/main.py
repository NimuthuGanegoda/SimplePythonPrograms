import os 
import shutil

def organize_files(main_folder):
    #Define folder mapping for file extensions
    extension_folders = {
        '.gif': 'Images',
        '.jpeg': 'Images',
        '.jpg': 'Images',
        '.png': 'Images',
        '.txt': 'Documents',
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.xlsx': 'Documents',
        '.pptx': 'Documents',
        '.zip': 'Compressed',
        '.mp3': 'Music',
        '.wav': 'Music',
        '.csv': 'Documents',
        '.py': 'Programs',
        '.exe': 'Programs',
        '.mp4': 'Videos',
        '.mkv': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
    }

    # Ensure all folder names are lowercase for consistency
    existing_folders = [folder.lower() for folder on os .listdir(main_folder)
                        ]