def count(text):
    result={}
    for word in text:
        if word not in result:
            result[word]=0
        result[word]+=1
    return result
print(count("ssrfgsfghsugs"))
print(count("mmmmmmmmmmmmm"))
print(count('this time we have a long dictionary letters'))