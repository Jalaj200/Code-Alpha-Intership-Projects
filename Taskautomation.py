import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all JPG files from source folder to destination folder.
    Creates destination folder if it doesn't exist.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Created directory: {destination_folder}")
        
        files = os.listdir(source_folder)
        moved_files = 0
        
        for file in files:
            if file.lower().endswith('.jpg'):
                src_path = os.path.join(source_folder, file)
                dst_path = os.path.join(destination_folder, file)
                
                shutil.move(src_path, dst_path)
                moved_files += 1
                print(f"Moved: {file}")
        
        print(f"\nOperation complete. Moved {moved_files} JPG files.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    source = input("Enter source folder path: ").strip()
    destination = input("Enter destination folder path: ").strip()
    move_jpg_files(source, destination)
