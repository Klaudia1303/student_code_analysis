s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
s3 = input ("inserire la stringa s3: ")
while ( len(s1)+len(s2) != len(s3)):
    s1 = s2
    s2 = s3
    s3 = input ("inserire la stringa s: ")
print (s1, s2, s3)
    
