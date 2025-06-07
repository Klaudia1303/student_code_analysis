s=input('inserire una stringa: ')
count=1
check=True
while check==True:
    if s.count('a')>0 and s.count('c')>0:
        check=False
    s=input('inserire una stringa: ')
    count=count+1
print(count)
