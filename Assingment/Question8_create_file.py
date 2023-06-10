import os

directory = 'C:/Users/mange/Desktop'
filename = 'myfile.txt'


file_path = os.path.join(directory, filename)


with open(file_path, 'w') as file:
    file.write("This is a new file.")

print(f"New file '{filename}' created in directory: '{directory}'.")
