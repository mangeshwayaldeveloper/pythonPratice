def skip_elements(elements):
    # code goes here
    result=[]
    for index, value in enumerate(elements):
        if index % 2 == 0:
           result.append(value)
    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
