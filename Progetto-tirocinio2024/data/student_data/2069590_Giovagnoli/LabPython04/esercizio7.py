s = input("Inserire una stringa: ")
i=0
massimo=0
while i<len(s):
    if massimo<=s.count(s[i]):
        if massimo==s.count(s[i]):
            carattere = s[i]
            if s.find(carattere)>massimo:
                massimo= s.count(carattere)
        massimo = s.count(s[i])
        i+=1
    else:
        i+=1
print("Il carattere che presenta maggiore occorennze è ", carattere)