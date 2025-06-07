ac=False
a=False
c=False
wordQuantity=1
while not ac:
    word=input('insert string: ')
    for count in range(len(word)):
        if word[count:count+1]=='a':
            a=True
            count+=1
        if word[count:count+1]=='c':
            c=True
            count+=1
        else:
            count+=1
    if a==True and c==True:
        ac=True
    else:
        count=0
        wordQuantity+=1
print(wordQuantity)