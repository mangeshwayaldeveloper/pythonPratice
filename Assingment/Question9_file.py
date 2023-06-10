def copy_file(source_file, destination_file):
 with open(source_file, 'r') as source:
  with open(destination_file, 'w') as destination:
   content = source.read()
   destination.write(content)


source_file = 'originfile.txt'
destination_file = 'blankFile.txt'

copy_file(source_file, destination_file)
print("Content copied successfully.")
