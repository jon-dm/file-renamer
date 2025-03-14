import os

folder_path = r"Your own folder path goes here!"
file_extensions = (".pdf", ".docx") # Add more extensions here, I use this to rename old resumes!

for filename in os.listdir(folder_path):
    if filename.lower().endswith(file_extensions):
        new_filename = "OLD - " + filename # Can change and mess around with how you want to rename your files here
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("Old resumes tagged.")


