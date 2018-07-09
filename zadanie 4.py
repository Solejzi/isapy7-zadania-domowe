print("podaj dowolna liczbe by dowiedziec sie jaka jest jej pierwsza oraz ostatnia cyfra")
liczba =input()
len(liczba)
print("pierwsza cyfra twojej liczby to", end=" ")
print(liczba[0])
print("a ostatnia cyfra to", end=" ")
print(liczba[len(liczba)-1])

#jak zrobic komunikat w razie gdyby ktos zamiast liczby wpisal litery lub znaki