s=input("Inserire una stringa: ")
run=False
for i in range(len(s)):
    v=s[i]
    if run==False:
        if s.count(v)>1:
            run=True
print(run)
