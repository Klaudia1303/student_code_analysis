s= input(' inserisci una stringa: ')
occorrenze=0
top=-1
T=''
for i in range(len(s)):
    if i ==len(s)-1:
        break
    if s[i]==s[i+1]:
        occorrenze+=1
    if occorrenze>=top and (s[i]!=s[i+1] or i ==len(s)-2):
        top=occorrenze
        I=i-1
        occorrenze=0
if i ==len(s)-1:
    print(s[I],top+1)
else:
    print(s[I],top+1)
