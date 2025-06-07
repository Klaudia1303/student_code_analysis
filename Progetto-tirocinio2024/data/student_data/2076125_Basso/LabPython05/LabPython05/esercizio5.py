

s=input("Inserire stringa: (almeno 2 caratteri)\t")
n=int(input("Inserire intero positivo:\t"))

for i in range(len(s)-n):
    if s[i]==s[i+n]:
        i=len(s)+1
if i==len(s)+1:
    print(True)
else:
    print(False)
