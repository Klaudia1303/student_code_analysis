s=input('inserire una stringa alfanumerica: ')
carattere=''
carattere1=''
caratteremax=''
for i in range(len(s)):
    if s[i]==s[i-1]:
        carattere=s[i]
        carattere1+=carattere
        if len(carattere1)>len(caratteremax):
            caratteremax=carattere1
    else:
        caratteremax=carattere1
        carattere1=''
        

print(caratteremax[0],len(caratteremax)+1)
        

        
        
   
    
    
