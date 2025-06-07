s = input("Inserisci una stringa: ")

last_i = ""
len_s = 0
max_len_s = 0

for i in s:
    if i == last_i:
        len_s += 1
        if len_s > max_len_s:
            max_len_s = len_s
    else:
            len_s = 1
            last_i = i
            
print(last_i, max_len_s)
    
        
        
    
    
