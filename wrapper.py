import os
import subprocess
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main(folders):
    """
    Process each folder with DJI thermal images.
    Processed images are saved in a subfolder 'output_images' inside each folder.
    
    Args:
        folders (list of str): List of directories to process
    """
    for folder in folders:
        abs_folder = os.path.abspath(folder)
        if not os.path.isdir(abs_folder):
            logging.warning(f"{abs_folder} is not a valid directory. Skipping.")
            continue
        
        logging.info(f"Processing folder: {abs_folder}")
        try:
            subprocess.run(
                ["python", "dji_thermal_converter.py", abs_folder],
                check=True
            )
        except subprocess.CalledProcessError:
            logging.error(f"Processing failed for {abs_folder}. Continuing with next folder.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python wrapper.py <folder1> <folder2> ...")
        sys.exit(1)

    # sys.argv[1:] contains all folders passed on the command line
    folders_to_process = sys.argv[1:]
    main(folders_to_process)
