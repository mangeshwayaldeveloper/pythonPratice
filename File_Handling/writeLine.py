f=open('writeLine.txt','w')
lines=['line one\n','line two\n','line three \n'] #we are writing here
f.writelines(lines)
f.close()