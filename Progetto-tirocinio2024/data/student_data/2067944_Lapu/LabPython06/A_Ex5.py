s=input("inserire una stringa: ")
carattere=""
occorrenze1=0
occorrenze=0
for i in s:
    for j in range(len(s)):
        if i == s[j:j+1]:
            carattere1=carattere
            occorrenze1+=1
    if occorrenze1>=occorrenze:
            occorrenze=occorrenze1
            carattere=carattere1
    occorrenze1=0
    carattere1=""
print(carattere,occorrenze)
