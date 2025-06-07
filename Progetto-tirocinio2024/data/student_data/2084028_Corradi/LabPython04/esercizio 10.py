s1 = input("insersici la stringa: ")
s2 = input("insersici la stringa: ")
s3 = input("insersici la stringa: ")
while len(s1) + len(s2) != len(s3):
    s1 = s2
    s2 = s3
    s3 = input("insersici la stringa: ")
print(s1,s2,s3)
