print("===Program Kalkulator Sederhana===")

x = float(input("Angka pertama: "))
op = str(input("Pilih operator: "))
y = float(input("Angka kedua: "))

def kalkulator(x,y,op):
    if op == '+':
        hasil = x+y
    elif op == '-':
        hasil = x-y
    elif op == '*':
        hasil = x*y
    elif op == '/':
        hasil = x/y
    else:
        hasil = 'error'
    return hasil

result = str(input("Continue? (Y/N)"))
if result == "Y":
    x = kalkulator(x,y,op)
    op = str(input("Pilih operator: "))
    y = float(input("Angka: ")) 
    print(kalkulator(x,y,op))
if result == "N":
    print(kalkulator(x,y,op))