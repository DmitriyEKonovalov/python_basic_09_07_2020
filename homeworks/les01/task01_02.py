# 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

secAmount = int(input("введите время в секундах: "))

hours = secAmount // 3600
minutes = (secAmount % 3600) // 60
seconds = secAmount % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
