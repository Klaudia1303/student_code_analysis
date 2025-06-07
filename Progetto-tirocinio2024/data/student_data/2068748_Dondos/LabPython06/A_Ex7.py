s1 = input('inserisci prima stringa: ')
s2 = input('inserisci seconda stringa: ')
max_seq = 0
first_char = 0
last_char = 0

for i in range(len(s2)):
    for j in range(i+1, len(s2)):
        if s2[i:j] in s1 and len(s2[i:j]) >= max_seq:
            max_seq = len(s2[i:j])
            fist_char = i
            last_char = j
print(s2[first_char:last_char])
