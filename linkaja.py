print("start")
print("pilih menu")
print("info saldo rp 1500000")

print("top up")
print("jumlah saldo awal rp 1500000")
c = eval(input("jumlah saldo yang di top up"))
d = 1500000 + c
print("saldo total linkaja rp", d)
e = 200000

f = eval(input("jumlah saldo yang ingin di ambil"))
g = 1500000 + c - f
if d > 20000:
     print("nilai saldo mencukupi")
else:
    print("nilai saldo tidak mencukupi")
print("saldo total linkaja Rp" ,f)