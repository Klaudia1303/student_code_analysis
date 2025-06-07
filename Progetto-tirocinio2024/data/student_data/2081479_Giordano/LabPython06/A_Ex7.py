word1=input('insert first word: ')
word2=input('insert second word: ')
matched=1
oldTopString=''
topString=''

for scan in range(len(word1)):

    for scan2 in range(len(word2)):
        if word1[scan:scan+matched]==word2[scan2:scan2+matched]:
            matchedStatus=True
            topString=word1[scan:scan+matched]
            while matchedStatus==True:
                matched+=1
                if word1[scan:scan+matched]==word2[scan2:scan2+matched]:
                    topString=word1[scan:scan+matched]
                else:
                    if len(oldTopString)<len(topString):
                        oldTopString=topString
                        matchedStatus=False
                if word1[scan:scan+matched]!=word2[scan2:scan2+matched]:    
                    topString=''
                    matchedStatus=False
                    matched=1
                if matched==len(word1):
                    break
print(oldTopString)