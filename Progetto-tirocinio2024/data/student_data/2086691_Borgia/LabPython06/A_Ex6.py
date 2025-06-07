per1=0
per2=0
for i in range(1,1000):
    per1=per1+20
    per2=per2+i
    if per1==per2:
        break
print(i)
