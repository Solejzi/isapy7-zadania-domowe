#pierwszy sposob robilem bez internetu wiec uznalem ze zrobie cokolwiek byle dzialalo
liczba_bin=(input("podaj liczbe w systemie binarnym (zapis 6 cyfrowy)"))


potega_1 = int(liczba_bin[-6])
potega_2 = int(liczba_bin[-5])
potega_3 = int(liczba_bin[-4])
potega_4 = int(liczba_bin[-3])
potega_5 = int(liczba_bin[-2])
potega_6 = int(liczba_bin[-1])
print(liczba_bin[-6], "* 32")
print(liczba_bin[-5], "* 16")
print(liczba_bin[-4], "* 8")
print(liczba_bin[-3], "* 4")
print(liczba_bin[-2], "* 2")
print(liczba_bin[-1], "* 1")

print("twoj wynik to:")
print((potega_1*32)+(potega_2*16)+(potega_3*8)+(potega_4*4)+(potega_5*2)+(potega_6*1))

#tu juz dostalem pomoc od kolegi
liczba_bin1 = input("wpisz liczbe w systemie binarnym")
suma = 0
for i in range(len(liczba_bin1)): #i[0, 1, 2, 3, ....]
    potega = len(liczba_bin1) - i - 1 #np. 000011  potega = 6 - 0 - 1, = 6 - 1 - 1, =6 - 2 - 1 ...
    skladnik = int(liczba_bin1[i])*(2**potega)
    suma += skladnik

print(suma)

