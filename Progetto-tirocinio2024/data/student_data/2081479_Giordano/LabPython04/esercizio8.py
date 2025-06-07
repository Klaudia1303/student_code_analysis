equal=False
startChar=''
endChar=''
oldString=''

while not equal:
    newString=input('insert string: ')
    startChar=newString[0:1]
    endChar=oldString[len(oldString)-1:len(oldString)]
    if startChar==endChar:
        equal=True
    else:
        oldString=newString
print(oldString,newString)