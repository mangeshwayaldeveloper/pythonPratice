lst = [i for i in range(4)]
print(lst)

# we can also did
lst1 = [i * i for i in range(4)]
print(lst1)

# -------------------------------------------
names = ['pooja', 'omkar', 'mango', 'old', 'pavan', 'rushi', 'gotuss']
SelectedName = [i for i in names if 'o' in i]
print(SelectedName)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TwoTable = [j for j in numbers if j % 2 == 0]
print(TwoTable)
