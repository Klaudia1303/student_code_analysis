s1 = input('inserisci prima stringa: ')
s2 = input('inserisci seconda stringa: ')
n = int(input('inserisci intero: '))
max_dist = n
same_char = ""
s3 = ""

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            same_char += s1[i]
            dist1 = s1.rfind(s1[i])-i
            dist2 = s2.rfind(s2[j])-j
            if dist1<=n:
                max_dist = dist1
            elif dist2<=n:
                max_dist = dist2
            
            
