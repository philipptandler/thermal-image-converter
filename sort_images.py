import os
import shutil
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def move_images(folder_path):
    """
    Moves files ending with '_T.JPG' or '_W.JPG' into their respective subfolders.
    Leaves all other files and directories untouched.
    """
    # Define target subfolders
    t_folder = os.path.join(folder_path, "Thermal_TJPG")
    w_folder = os.path.join(folder_path, "RGB_WJPG")

    # Create subfolders if they don't exist
    os.makedirs(t_folder, exist_ok=True)
    os.makedirs(w_folder, exist_ok=True)

    # Loop through all items in the folder (non-recursive)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Move matching files
        if item.endswith("_T.JPG"):
            shutil.move(item_path, os.path.join(t_folder, item))
        elif item.endswith("_W.JPG"):
            shutil.move(item_path, os.path.join(w_folder, item))
    
    logging.info(f"All files moved in {folder_path}")

def main(folders):
    """
    Process each folder with DJI thermal images and wide angle RGB images.
    """
    for folder in folders:
        abs_folder = os.path.abspath(folder)
        if not os.path.isdir(abs_folder):
            logging.warning(f"{abs_folder} is not a valid directory. Skipping.")
            continue
        
        logging.info(f"Processing folder: {abs_folder}")
        move_images(abs_folder)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python sort_images.py <folder1> <folder2> ...")
        sys.exit(1)

    # sys.argv[1:] contains all folders passed on the command line
    folders_to_process = sys.argv[1:]
    main(folders_to_process)