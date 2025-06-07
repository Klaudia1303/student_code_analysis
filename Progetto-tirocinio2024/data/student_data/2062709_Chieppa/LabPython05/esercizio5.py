s=str(input('inserire stringa: '))
n=int(input('inserire intero positivo: '))
check=False
for i in range(len(s)):
    if s.find(s[i])-s.rfind(s[i])==n:
        check=True
print(check)
