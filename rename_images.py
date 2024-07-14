import os


def rename_images(folder_path):
  """
  This function renames all image files in a folder to a sequence starting with 'a'
  and a number (e.g., a1.jpg, a2.jpg, etc.) in ascending order.

  Args:
      folder_path: The path to the folder containing the images.
  """
  counter = 1
  for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
      # Optional image verification using Pillow
        new_filename = f"a{counter}.{filename.split('.')[-1]}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1

# Replace with the actual path if not the current directory
path1 = r"E:\biodatas\new"
folder_path = path1
rename_images(folder_path)
print("Images renamed successfully!")