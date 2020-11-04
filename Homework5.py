# ДЗ5

revenue = int(input("Сообщите налоговой вашу выручку: "))
lesion = int(input("Замечательно. Теперь сообщите ваши убытки: "))

res = revenue - lesion
if res == 0:
    print("Вы работаете средне. Старайтесь")
elif res < 0:
    print("Плохо работаете! Досвидания!")
else:
    print("Вы хорошо работаете!")

rent = (revenue / lesion)
print(f"Ваше рентабельность составляет: {rent}%")

people = int(input("А скажите, сколько сотрудников у вас работает:"))

rent_people = res / people
print("Значит на каждого сотрудника приходится", rent_people)


