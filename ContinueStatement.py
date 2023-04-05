inputByUser=int(input("Enter Your Input"))
for i in range(12):
    if(i==10):
        print("Continue to next statement for this operation")
        continue
    print(inputByUser,"X",i,"= ",inputByUser*i)
