import random

karakter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
panjang = int(input('Jumlah karakter: '))

sandi = ""

for p in range(panjang):
    sandi += random.choice(karakter)

print(sandi)
