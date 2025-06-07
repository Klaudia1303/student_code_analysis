s=input('Inserire una stringa: ')
dis=0
for i in s:
    c=(s.rfind(i))-(s.find(i))
    if c>dis:
        dis=c
print(dis)
