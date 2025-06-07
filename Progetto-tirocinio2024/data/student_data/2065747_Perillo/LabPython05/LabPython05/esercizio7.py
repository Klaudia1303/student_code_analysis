s=input("Inserire una stringa:")
a="False"
for i in s:
    if s.count(i)>1:
        a="True"
print(a)
