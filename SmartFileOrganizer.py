import os 
import shutil

def organize_files(main_folder):
    #Define folder mapping for file extensions
    extension_folders = {
        # Images
        '.gif': 'Images', '.jpeg': 'Images', '.jpg': 'Images', '.png': 'Images', '.bmp': 'Images', '.tiff': 'Images', '.svg': 'Images', '.webp': 'Images', '.ico': 'Images',
        # Documents
        '.txt': 'Documents', '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.xls': 'Documents', '.xlsx': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents', '.csv': 'Documents', '.rtf': 'Documents', '.odt': 'Documents', '.ods': 'Documents', '.odp': 'Documents', '.tex': 'Documents', '.epub': 'Documents', '.md': 'Documents', '.log': 'Documents',
        # Archives/Compressed
        '.zip': 'Compressed', '.rar': 'Compressed', '.tar': 'Compressed', '.gz': 'Compressed', '.bz2': 'Compressed', '.7z': 'Compressed', '.xz': 'Compressed', '.iso': 'Compressed', '.tgz': 'Compressed', '.lz': 'Compressed',
        # Music/Audio
        '.mp3': 'Music', '.wav': 'Music', '.aac': 'Music', '.flac': 'Music', '.ogg': 'Music', '.wma': 'Music', '.m4a': 'Music', '.aiff': 'Music', '.alac': 'Music', '.amr': 'Music',
        # Video
        '.mp4': 'Videos', '.mkv': 'Videos', '.avi': 'Videos', '.mov': 'Videos', '.flv': 'Videos', '.wmv': 'Videos', '.webm': 'Videos', '.mpeg': 'Videos', '.mpg': 'Videos', '.m4v': 'Videos', '.3gp': 'Videos', '.ts': 'Videos', '.vob': 'Videos',
        # Programs/Code
        '.py': 'Programs', '.exe': 'Programs', '.bat': 'Programs', '.sh': 'Programs', '.js': 'Programs', '.ts': 'Programs', '.java': 'Programs', '.c': 'Programs', '.cpp': 'Programs', '.cs': 'Programs', '.rb': 'Programs', '.php': 'Programs', '.go': 'Programs', '.swift': 'Programs', '.pl': 'Programs', '.r': 'Programs', '.html': 'Programs', '.css': 'Programs', '.json': 'Programs', '.xml': 'Programs', '.yml': 'Programs', '.yaml': 'Programs', '.ipynb': 'Programs', '.db': 'Programs', '.sqlite': 'Programs', '.apk': 'Programs', '.jar': 'Programs', '.msi': 'Programs', '.ps1': 'Programs', '.vb': 'Programs', '.lua': 'Programs', '.scala': 'Programs', '.dart': 'Programs', '.kt': 'Programs', '.m': 'Programs', '.h': 'Programs', '.asm': 'Programs', '.sln': 'Programs', '.vbproj': 'Programs', '.vcxproj': 'Programs', '.xcodeproj': 'Programs',
        # System Files
        '.ini': 'System Files', '.icc': 'System Files', '.sys': 'System Files', '.dll': 'System Files', '.drv': 'System Files', '.cfg': 'System Files', '.bak': 'System Files', '.tmp': 'System Files', '.bin': 'System Files', '.dat': 'System Files', '.dmp': 'System Files', '.lnk': 'System Files', '.swp': 'System Files', '.lock': 'System Files', '.old': 'System Files', '.log': 'System Files',
        # Fonts
        '.ttf': 'Fonts', '.otf': 'Fonts', '.woff': 'Fonts', '.woff2': 'Fonts', '.eot': 'Fonts',
        # Others
        '.eml': 'Emails', '.msg': 'Emails', '.ics': 'Calendar', '.vcf': 'Contacts', '.torrent': 'Torrents', '.apk': 'Mobile Apps', '.ipa': 'Mobile Apps', '.deb': 'Packages', '.rpm': 'Packages', '.msi': 'Packages', '.app': 'Packages', '.pkg': 'Packages',
    }

    # Ensure all folder names are lowercase for consistency
    existing_folders = [folder.lower() for folder in os.listdir(main_folder)
                       if os.path.isdir(os.path.join(main_folder, folder))]

    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            if ext in extension_folders:
                folder_name = extension_folders[ext]
                target_folder = os.path.join(main_folder, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(item_path, os.path.join(target_folder, item))
                # Determine target folder name
                target_folder = extension_folders[ext]

                # Check if folder already exits (case insensitive)
                if target_folder.lower() not in existing_folders:
                    os.markdir(os.path.join(main_folder, target_folder),
                    exist_ok=True)
                    existing_folders.append(target_folder.lower())
                
                # Move file to the appropriate folder
                shutil.move(item_path, os.path.join(main_folder,target_folder, item))
                print(f"Moved: {item} -> {target_folder}")
            else: 
                print(f"Skipping: {item} -> (No folder mapping)")


if __name__ == "__main__":
    folder = input("Enter the path to the folder you want to organize: ").strip()
    if os.path.isdir(folder):
        organize_files(folder)
        print(f"Files in '{folder}' have been organized.")
    else:
        print("Invalid folder path.")