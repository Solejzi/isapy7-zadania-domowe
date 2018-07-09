wartosc = input("podaj rok")
rok = int(wartosc)

if rok%400 == 0:
    print("twoj rok jest rokiem przestepnym")
elif rok%4 == 0 and rok%100 != 0:
    print("twoj rok jest rokiem przestepnym")
else:
    print("twoj rok nie jest rokiem przestenpnym")



import calendar
data = input("podaj rok")

if (calendar.isleap(int(data))) == False:
    print('twoj rok nie jest rokiem przestepnym')
else:
    print('twoj rok jest rokiem przestepnym')
