f=open('file.txt','w')
text=f.write('i am writing in this file this content will be show to me \n'
             'i am using some characters which will provide new line.')
f=open('file.txt','r')
print(text)
text=f.read()
print(text)
f.close()