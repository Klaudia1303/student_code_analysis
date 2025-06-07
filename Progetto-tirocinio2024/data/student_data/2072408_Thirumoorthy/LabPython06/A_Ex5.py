s=input('inserire una stringa alfanumerica')
k=''
occor=0
for i in range(len(s)):
    ch=s[i]
    occ=0
    for j in range(len(s)-i):
        if ch==s[i+j]:
            occ+=1
        else:
            break
    if occor<=occ:
        ch=k 
        occ=occor
       
print(k,occor)
