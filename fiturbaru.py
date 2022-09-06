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

print(kalkulator(x,y,op))