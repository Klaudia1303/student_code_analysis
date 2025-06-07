s = input("Inserisci una stringa: ")
n = int(input("Inserisci un intero: "))

for i in range(len(s)):
    m = s[i]*n
    print(m,sep = "", end = "")
