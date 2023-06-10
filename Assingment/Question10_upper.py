def count_lower_chars(string):
 upper_count = 0
 lower_count = 0

 for char in string:
  if char.isupper():
   upper_count += 1
  elif char.islower():
   lower_count += 1

 return upper_count, lower_count


input_string = input("Enter a string: ")

upper_chars, lower_chars = count_lower_chars(input_string)

print("Total uppercase characters:", upper_chars)
print("Total lowercase characters:", lower_chars)
