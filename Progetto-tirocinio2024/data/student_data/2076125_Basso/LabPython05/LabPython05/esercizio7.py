

s=input("Inserire stringa:\t")

for i in s:
    if s.count(i)>=2:
        i='*'
if i=="*":
    print(True)
else:
    print(False)
    
