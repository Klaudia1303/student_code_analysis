s = input("Stringa: ")

occorrenze_cons_max = 0
c_max = ""
for i in range(len(s)):
    occorrenze_cons=1
    for j in range(i+1, len(s)):
        if s[j] != s[i]:
            break
        occorrenze_cons += 1
    if occorrenze_cons >= occorrenze_cons_max:
        occorrenze_cons_max = occorrenze_cons
        c_max = s[i]
print(c_max, occorrenze_cons_max)
