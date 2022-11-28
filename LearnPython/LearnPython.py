def number_of_integers_in_the_interval_x_and_y(x,y):
    res = 0
    while x != y:
        if x % 2 == 0 or x % 3 == 0:
            res += 1
        
        x -=1
        
    return res


print("Задание 1")

print("Введите x")
x = int(input())

print("Введите y")
y = int(input())

res = 0

if x == y:
    print("x и y равны, чисел, делящихся на 2 и 3 нет")
elif x > y:
    print(number_of_integers_in_the_interval_x_and_y(x,y))
elif y > x:
    print(number_of_integers_in_the_interval_x_and_y(y,x))

print("Задание 2")

print("Введите x")

x = int(input())

one_max_number = 0
two_max_number = 0
if x < 1:
    print("x должен быть больше 1")
else: 
    while x != 0:
        num = int(input())
        if num  > one_max_number:
            two_max_number = one_max_number
            one_max_number = num
        elif num > two_max_number:
            two_max_number = num
        x-=1
    print(f"максимальное число {one_max_number}, второе максимальное число {two_max_number}")

print("Задание 3")

x = int(input())

denomination_banknote_25 = 0
denomination_banknote_10 = 0
denomination_banknote_3 = 0
denomination_banknote_1 = 0

while x != 0:
    if x - 25 >= 0:
        x -= 25
        denomination_banknote_25 +=1
    elif x - 10 >= 0:
        x -= 10
        denomination_banknote_10 += 1
    elif x - 3 >= 0:
        x -= 3
        denomination_banknote_3 += 1
    elif x - 1 >= 0:
        x -= 1
        denomination_banknote_1 += 1

print(f"25 - {denomination_banknote_25}, 10 - {denomination_banknote_10}, 3 - {denomination_banknote_3}, 1 - {denomination_banknote_1}")

print("Задание 4")

print("Введите x")

x = int(input())

result = []
while x > 0:
    result.append(x % 10)
    x //= 10

result.reverse()

flag = True

length = len(result)

i = 0

while i != length:
    if i == length - 1:
        break
    else:
        if result[i] >= result[i + 1]:
            flag = False
    
    i += 1

if flag: 
    print ("Да")
else:
    print("Нет")