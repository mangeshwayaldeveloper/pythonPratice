letter="Hey my name is {} and, I am from {}"
name="Mangesh"
city="Jalna"
# print(letter.format(name,city))
print(letter.format(city,name))

'''The above apporach of formating is the old approach
which is used before python 3.6.
in this approach it is not convienient to rember sequence of
variables'''
# New Approach
print(f"Hey my name is {name} and, I am from {city}")
price=49.22222343
txt=f"For Only Price {price:.2f} dollars!"
print(txt)

# print exact row string
'''this will print the string as it is 
whithout replacing'''
print(f"Hey my name is {{name}} and, I am from {{city}}")
price=49.22222343
txt=f"For Only Price {price:.2f} dollars!"
print(txt)