s1 = input("s1: ")
s2=input( "s2: ")
max_seq=""
seq=""
inizio=0
for i in range(len(s1)):
    for j in range(inizio, len(s2)):
        print(s1[i],s2[j])
        if sl[i]==s2[j]:
            inizio = j+1
            seq=seq +s2[j]
            break
        else:
            if len(seq) >len(max_seq):
                max_seq=seq
                seq=""
                inizio=0
                i-=i
print(max_seq)
