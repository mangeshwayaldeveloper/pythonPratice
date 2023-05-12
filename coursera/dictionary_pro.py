def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for key,value in countries_dict.items():
        # Use a string method to format the required string.
        value=countries_dict[key]
        result +=str(value)+"\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']