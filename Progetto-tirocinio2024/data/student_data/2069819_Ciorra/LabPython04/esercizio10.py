s1=input("stringa1")
s2=input("stringa2")
s3=input("stringa3")
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3=input("inserisci una stringa: ")
print(s1,s2,s3) 


    
