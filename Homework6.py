# ДЗ6

a = int(input("В первый день спортсмен пробежал километров: "))
b = int(input("Результат должен составить не менее: "))
day = 1
while a <= b:
    a *= 1.1
    day = day + 1
    print(a)
print(f"Результат будет достигнут на {day} день!")