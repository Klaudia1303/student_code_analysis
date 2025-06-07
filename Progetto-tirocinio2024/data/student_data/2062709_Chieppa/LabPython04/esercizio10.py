s1 = input('Inserire stringa 1: ')
s2 = input('Inserire stringa 2: ')
s3 = input('Inserire stringa 3: ')
while len(s1)+len(s2)!=len(s3):
    s1 = s2
    s2 = s3
    s3 = input('Inserire una stringa: ')
print(s1,s2,s3)
           
        
    
