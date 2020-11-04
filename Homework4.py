# ДЗ 4

numb = int(input("Введите целое положительное число: "))
x = -1
if numb < 10:
    x = numb
while numb > 10:
    d = numb % 10
    numb //= 10
    if d > x:
        x = d
print("Наибольшее число: ", x)