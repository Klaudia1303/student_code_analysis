#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.5

s = input("Inserire una stringa: ");
count = 0;
lettera = 0;
count2 = 0;
lettera2 = 0;
for i in range(-1, len(s)):
    if i < len(s)-1:
        if s[i] == s[i+1]:
            if i > 0:
                if lettera != s[i] or lettera2 != s[i]:
                    count2 += 1;
                    lettera2 = s[i];
                else:
                    lettera = s[i];
                    count += 1;
                    
                if count2 > count:
                    count = count2;
                    lettera = lettera2
                    count2 = 0;
                    lettera2 = 0;
            else:
                lettera = s[i];
                count += 1;
        elif s[i] == s[i-1]:
            count +=1;
    if i == len(s)-1:
        if lettera == s[i]:
            count +=1;
print(lettera, count);