import os

# Specify the path to the folder
folder_path = r'C:\Users\DSF20220704001\OneDrive\바탕 화면\test_filename'

# Iterate through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Split the filename into base and extension
        base, extension = os.path.splitext(filename)

        # Check if the filename contains the '_' character
        if '_' in base:
            # Reverse the order of the base name using the '_' delimiter
            new_base = '_'.join(reversed(base.split('_')))

            # Construct the new filename by combining the reversed base name and extension
            new_filename = new_base + extension

            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'.")
