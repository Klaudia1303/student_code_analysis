s = input("Inserisci stringa: ")
t = 0
l2 = int(len(s)/2)

for i in range(0, len(s)):
    for n in range(len(s)-1, l2-1, -1):
        if (s[i]==s[n] and i!= n and t==i):
            t=t+1
print(int(t))
