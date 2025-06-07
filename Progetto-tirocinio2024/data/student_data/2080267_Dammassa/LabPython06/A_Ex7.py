s1 = input("stringa: ")
s2 = input("stringa: ")

len_max = 0
s_max = " "
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        s = s1[i:j]
        if s in s2:
            l = j - i
            if l >= len_max:
                len_max = l
                s_max = s
            else:
                break
print(s_max)
            
