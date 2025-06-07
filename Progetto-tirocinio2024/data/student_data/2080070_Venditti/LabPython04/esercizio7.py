n=input('inserire una stringa: ')
i=0
count=0
count2=0
while i<len(n):
    count=n.count(n[i-1])
    if count>count2:
        count2=count
        s1=n[i-1]
    i+=1
print(s1)
    
