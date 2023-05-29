f=open('file.txt')
while True:
    line=f.readline()
    if not line:
        break
    print(line)