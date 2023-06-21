m = int(input("Введите номер месяца: "))
if m <= 6:
 print("Первое полугодие")
else:
 print("Второе полугодие")

if m == 2:
 days = 28
elif m in [4, 6, 9, 11]:
 days = 30
else:
 days = 31

print("Количество дней в месяце:", days)
