s=input("immetti una stringa: ")
compare=False
for i in s:
    if s.find(i)!=s.rfind(i):
        compare=True
print(compare)
