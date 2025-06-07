s=input('please enter a word: ')
found=False
while not found:
    lastChr=s[len(s)-1]
    lastStr=s
    usrString=input('please enter another word: ')
    if lastChr==usrString[0]:
        found=True
    else: s=usrString
print(lastStr,usrString)
