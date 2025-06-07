s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stirnga: ")
n = int(input("Inserisci un intero: "))

news = ""

for i in range(len(s1)):
    c = s1[i]
    if c in s2[max(0, i - n) :min(len(s2), i + n)]:
        news += c
print(news)
            
