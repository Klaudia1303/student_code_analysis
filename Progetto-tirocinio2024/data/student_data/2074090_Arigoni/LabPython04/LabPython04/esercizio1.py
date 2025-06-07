carattere=["a","c"]

finito=True
count=0
while finito:
    s=input("Inserisci una stringa: ")
    if "c" and "a" in s:
        finito=False
    count=count+1
print(count)
