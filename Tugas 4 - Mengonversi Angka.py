x = int(input("Masukkan angka: "))

a = bin(x)[2:].zfill(8)
b = oct(x)[2:].zfill(8)
c = hex(x)[2:].zfill(8)

print("Biner:", (a))
print("Oktal:", (b))
print("Desimal:", x)
print("Heksadesimal:", (c))
