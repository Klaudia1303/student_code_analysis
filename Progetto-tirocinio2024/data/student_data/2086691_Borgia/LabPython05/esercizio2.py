s=input("Inserire una stringa: ")
n=int(input("Inserire un intero positivo: "))
stot=''
for i in range(len(s)):
    stot=stot+(s[i]*n)
print(stot)
