try:
    f=open("file.html")
    text=f.read()
    print(text)
    f.close()
except Exception as e:
    print(e)
