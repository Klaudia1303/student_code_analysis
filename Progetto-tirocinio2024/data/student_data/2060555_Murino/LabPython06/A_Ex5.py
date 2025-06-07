s=input('inserisci la stringa: ')
occorenze=0
top=-1
for i in range(len(s)):
    if i==len(s)-1:
        break
    if s[i]==s[i+1]:
        occorenze+=1
    if occorenze>=top and (s[i]!=s[i+1] or i==len(s)-2):
        top=occorenze
        I=i-1
        occorenze=0
if i==len(s)-1:
    print(s[I], top+1)
else:
    print(s[I], top)
        
