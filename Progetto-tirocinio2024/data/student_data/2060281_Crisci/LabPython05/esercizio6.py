s=str(input("Inserire una stringa: "))
max=0
for i in range((len(s)-1)):
    d=s.rfind(s[i])-i
    if(d>max):
        max=d
print(max)
