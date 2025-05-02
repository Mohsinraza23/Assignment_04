import os

def bulk_rename(folder_path, prefix="File_", change_ext=None):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        count = 1

        for file_name in files:
            old_path = os.path.join(folder_path, file_name)

            # Skip folders
            if os.path.isdir(old_path):
                continue

            # Get file extension
            _, ext = os.path.splitext(file_name)
            new_ext = change_ext if change_ext else ext

            # New file name
            new_name = f"{prefix}{count}{new_ext}"
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} → {new_name}")
            count += 1

        print("\nRenaming complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder = input("Enter the full path to the folder: ").strip()
    prefix = input("Enter a prefix for new files (default is 'File_'): ").strip() or "File_"
    change_ext = input("Enter new file extension (e.g., .txt) or leave blank to keep original: ").strip()
    if not change_ext.startswith('.') and change_ext:
        change_ext = '.' + change_ext  # Ensure it starts with dot

    bulk_rename(folder, prefix, change_ext or None)
