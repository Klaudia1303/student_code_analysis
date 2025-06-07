s=input('inserire una strga: ')
i=0
indice=False 
while  i<len(s) and not indice:
    if s.count(s[i])>1:
        indice=True
    else:
        i+=1
print(indice)
