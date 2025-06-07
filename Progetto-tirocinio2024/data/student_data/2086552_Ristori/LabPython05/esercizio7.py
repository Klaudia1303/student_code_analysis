s=str(input("Inserire una stringa:"))
for i in range(len(s)):
    if s.count(s[i])>=2:
        b=True
    else:
        b=False
if b:
    print("True")
else:
    print("False")
