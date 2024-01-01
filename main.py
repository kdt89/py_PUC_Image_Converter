import configparser
from datetime import datetime
import os
from os import path


# Read configuration from INI file
config = configparser.ConfigParser()
config.read("option.ini")

# Get the current working dir
cwd = path.abspath(path.dirname(__file__))

# Check if output folder exists, create if not
output_dir = os.path.join(cwd, "Output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get the path to Input data (folder contains images to be converted to JPG)



# # Loop through all subfolders in the specified path
# for subfolder in os.listdir(search_dirs):
#     subfolder_path = os.path.join(search_dirs, subfolder)
#     for search_dir in search_dirs:
        


#     # Look for the image file in the subfolder
#     image_path = os.path.join(subfolder_path, image_file_name_to_get)
#     if os.path.exists(image_path):
#         # Convert TIF to JPG using IrfanView
#         output_filename = os.path.splitext(image_file_name_to_get)[0] + ".jpg"
#         output_path = os.path.join(search_dirs, output_filename)
#         command = f"i_view64.exe \"{image_path}\" /advancedbatch /convert=.\\output\\\"{output_filename}\""
#         subprocess.run(command, shell=True)

# # Update FROM_DATE in INI file
# config["DEFAULT"]["FROM_DATE"] = str(current_date)
# with open("config.ini", "w") as f:
#     config.write(f)

# Exit program
print(f"Finished converting TIFs to JPGs")
exit()