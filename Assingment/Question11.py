def count_lines(filename):
 with open(filename, 'r') as file:
  lines = file.readlines()
  line_count = len(lines)
 return line_count


filename = input("Enter the filename: ")

try:
 line_count = count_lines(filename)
 print("Number of lines:", line_count)
except FileNotFoundError:
 print("File not found. Please check the filename and try again.")
