var1=str(input("Inserire una stringa palindroma:"))
b=True
while b:
    if var1==var1[-1::-1]:
        print("stringa palindroma di lunghezza:",len(var1))
        b=False
    else:
        var1=str(input("Non palindroma.Inserire una stringa palindroma:"))
    
