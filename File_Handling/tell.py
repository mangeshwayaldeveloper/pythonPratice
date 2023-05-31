with open('file.txt') as f:
    data=f.read()
    f.seek(10)
    pos=f.tell()
    print(pos)

