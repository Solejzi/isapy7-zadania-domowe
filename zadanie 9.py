wartosc = input("podaj wartosc")
a = int(wartosc)
if a%3 == 0 and a%5 == 0 and a%7 == 0:
    print("twoja liczba jest podzielna przez 3, 5 oraz 7")
else:
    print("twoja liczba nie spelnia warunkow (nie jest podzielna prez 3,5 i 7)")