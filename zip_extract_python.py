import os
from zipfile import ZipFile

# Get the current working directory
path1 = r"E:\biodatas\new"
current_dir = path1

# Iterate through all files in the directory
for filename in os.listdir(current_dir):
  # Check if the file ends with .zip extension (case-insensitive)
  if filename.lower().endswith(".zip"):
    # Create a ZipFile object
    print(filename)
    file2 = path1 + "\\" +filename
    with ZipFile(file2, 'r') as zip_ref:
      # Extract all files to the current directory
      zip_ref.extractall(current_dir)
      print(f"Extracted: {filename}")
    
