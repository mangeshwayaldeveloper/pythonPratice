f=open("file.txt",'a')
text=f.write("This content should go after the content which is already exists in file")
f=open('file.txt','r')
text=f.read()
print(text)