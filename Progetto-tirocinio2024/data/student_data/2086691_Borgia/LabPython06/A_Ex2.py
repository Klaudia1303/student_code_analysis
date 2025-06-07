s=input("Inserire una sringa: ")
run=True
for i in range(len(s)):
    if run==True:
        if s[i]==s[-i-1]:
            v=i+1
        else:
            run=False
print('Livello',v)
