'''wartosc = input("podaj liczbe a powiem ci czy jest podzielna przez 3 lub 5 lub 7")
a =int(wartosc)
def fraza():
    print("twoja liczba jest podzielna przez")
if a%3 == 0 and a%5 == 0 and a%7 == 0:
    fraza()
    print("3, 5 i 7")
elif a%3 == 0 and a%5 == 0:
    fraza()
    print("3 i 5")
elif a%3 == 0 and a%7 == 0:
    fraza()
    print("3 i 7")
elif a%5 == 0 and a%7 == 0:
    fraza()
    print("5 i 7")
elif a%3 == 0:
    fraza()
    print("3")
elif a%5 == 0:
    fraza()
    print("5")
elif a%7 == 0:
    fraza()
    print("7")
else:
    print("nie jest podzielna przez zadna z tych liczb")'''

wartosc = input("podaj liczbe a powiem ci czy jest podzielna przez 3 lub 5 lub 7")
a =int(wartosc)
def fraza():
    print("twoja liczba jest podzielna przez")
fraza()
if a%3 == 0:
    print("3")
if a%5 == 0:
    print("5")
if a%7 == 0:
    print("7")
if a%3 != 0 and a%5 != 0 and a%7 != 0:
    print('nie jest podzielna przez zadna z tych liczba')

