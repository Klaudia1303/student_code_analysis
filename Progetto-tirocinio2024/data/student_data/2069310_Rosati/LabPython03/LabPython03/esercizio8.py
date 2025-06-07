s=input("inserire una stringa palindroma: ").lower()
while s!=s[::-1]:
      s=input("Non palindroma,inserire una stringa palindroma: ").lower()
print("stringa palindroma di lunghezza",len(s))
      
