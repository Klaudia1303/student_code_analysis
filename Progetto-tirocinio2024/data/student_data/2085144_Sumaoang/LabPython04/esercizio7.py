s = input("Inserire una stringa non vuota:")
i = 0
carattere = ""
occorrenzeCarattere = 0

while i < len(s):
    carattereToScan = s[i]
    totalCountCarattere = s.count(carattereToScan)
    if totalCountCarattere >= occorrenzeCarattere:
        occorrenzeCarattere = totalCountCarattere
        carattere = carattereToScan
    i += 1
print(carattere)
    
