s1=input('inserire una stringa: ')
s2=input('inserire una stringa: ')

i=True
while i==True:
      s3=input('inserisci una stringa: ')
      if len(s1)+len(s2)==len(s3):
            i==False
            print(s1,s2,s3)
      else:
            s1=input('inserire una stringa: ')
            if len(s2)+len(s3)==len(s1):
                  print(s2,s3,s1)
                  i==False
            else:
                  s2=input('inserire una stringa: ')
                  if len(s3)+len(s1)==len(s2):
                        print(s3,s1,s2)
                        i==False
            

            