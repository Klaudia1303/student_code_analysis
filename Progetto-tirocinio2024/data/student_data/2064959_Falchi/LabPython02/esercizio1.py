hh = int(input("Inserire ore: "))
mm = int(input("Inserire minuti: "))
ss = int(input("Inserire secondi: "))

HH_to_SS = hh*60*60
MM_to_SS = mm*60

Result = HH_to_SS + MM_to_SS + ss

print(str(hh)+"h", str(mm)+"m", str(ss)+"s =", str(Result))
