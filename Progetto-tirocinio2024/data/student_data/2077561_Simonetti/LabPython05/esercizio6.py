string=input('please enter a word: ')
found=False
i=0
while not found and i<=len(string)-1:
    if string.count(string[i])>1:
        print(string.rfind(string[i])-i)
        found=True
    else: i+=1
    if i==len(string)-1 and found==False:
        print('0')

        
