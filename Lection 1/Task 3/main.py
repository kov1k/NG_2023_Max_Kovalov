temperature = int(input("Введіть температуру яку необхідно перевести: "))
print("1 - Цельсія у Фаренгейти\n2 - Фаренгейти в Цельсія")
choise = int(input(": "))

if choise == 1:
    result = (temperature - 32) / 1.8 
    print(f"{result}°F")
elif choise == 2:
    result = temperature * 1.8 + 32
    print(f"{result}°C")
else:
    print("Невірний варіант вибору.")
    