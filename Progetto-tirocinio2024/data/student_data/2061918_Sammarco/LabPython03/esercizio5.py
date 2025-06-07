corretto=False
while not corretto:
    S=input("inserisci una stringa")
    print(S[0]+S[-1])
    if S.isalpha() and S.islower():
        corretto=True
