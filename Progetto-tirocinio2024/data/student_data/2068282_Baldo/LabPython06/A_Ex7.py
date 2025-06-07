s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa: ")

s_max = ""
len_max = 0

for i in range(len(s1)):
    for j in range(i +1, len(s1) + 1):
        s = s1[i:j]
        if s in s2:
            l = j - i
            if l >= len_max:
                len_max = l
                s_max = s
        else:
            break
print(s_max)
            
    
