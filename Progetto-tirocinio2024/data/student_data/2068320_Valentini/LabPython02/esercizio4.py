s=input("Inserire una stringa di testo non vuota: ")
l=len(s)
if s[0]==s[l-1]:
    print("Caratteri iniziali e finali uguali")
else:
    print("Caratteri iniziali e finali diversi")
