s=str(input("Inserire una stringa: "))
ripetizione=False
for i in range(len(s)-1):
    if(i!=s.rfind(s[i])):
        ripetizione=True
print(ripetizione)
