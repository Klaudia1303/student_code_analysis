s=input("Insrisci stringa :")
liv=0
for i in range(len(s)):
    if s[i]==s[0-(i+1)]:
        liv +=1
    else:
        break
print("Parola palindroma di",liv,"livello")
