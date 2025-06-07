s=input('inserire una stringa: ')
k=0
for i in s:
    if s.count(i)>1:
        print(True)
        break
    else:
        k=k+1
if k==len(s):
    print(False)
