print("inserire due stringhe della stessa lunghezza")
s1=input("inserire stringa n1: ")
s2=input("inserire stringa n2: ")
s3=""
for i in range(0, len(s1)):
    s3+=s1[i]+s2[i]

print(s3)
