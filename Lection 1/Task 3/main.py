temperature = int(input("Введите температуру которую хотите перевести: "))
print("1 - Цельсия в Фаренгейты\n2 - Фаренгейты в Цельсия")
choise = int(input(": "))

if choise == 1:
    result = (temperature - 32) / 1.8 
    print(f"{result}°F")
elif choise == 2:
    result = temperature * 1.8 + 32
    print(f"{result}°C")
else:
    print("Неправильный вариант выбора.")
    