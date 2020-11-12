# ДЗ 2

print("Добро пожаловать в конвертор секунд")
second = int(input("Введите кол-во секунд: "))
hour = 60 * 60
minute = 60

h = second // hour
m = (second - (h * hour)) // minute
s = second - ((h * hour) + (m * minute))

print(f"Итого времени: {h} часов {m} минут {s} секунд")