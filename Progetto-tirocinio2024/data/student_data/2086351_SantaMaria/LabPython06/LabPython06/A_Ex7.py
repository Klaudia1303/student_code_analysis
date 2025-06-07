s1=input('Inserire una stringa: ')
s2=input('Inserire una stringa: ')
seq=''
for i in range(len(s1)):
    for k in range(len(s1)+1):
        if s1[i:k] in s2 and len(s1[i:k])>len(seq):
            seq=s1[i:k]
print(seq)
