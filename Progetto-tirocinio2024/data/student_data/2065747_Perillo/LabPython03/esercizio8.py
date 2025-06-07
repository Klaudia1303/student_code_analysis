s=input("inserire una parola palindroma")
l=len(s)
n=int(-2)
m=1
while m<=len(s):
         if s[m:m+1]==s[n:n+1] and s[0]==s[-1]:
            m=m+1
            n=n-1
         else:
            print("la parola non è palindroma")
            s=input("inserire una parola palindroma")
print(len(s))
    
