s=input("Inserire una stringa:")
a=0
for i in s:
    if s.rfind(i)>0:
        if s.rfind(i)-s.find(i)>a:
            a=s.rfind(i)-s.find(i)
print(a)
