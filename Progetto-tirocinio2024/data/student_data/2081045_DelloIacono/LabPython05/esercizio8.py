s = int(input("Inserire numero: "))
for i in range(s):
    if(i%2!=0 and i!=0):
        sSpazio = (s - i)//2
        print((' '*sSpazio)+('*'*i))
print('*'*s)
