s = input("inserisci la stringa: ")
max_=s[0]
for i in range(len(s)-1):
    if s.count(s[i]) < s.count(s[i+1]):
        max_=s[i+1]
print(max_,s.count(max_))
        
    
        