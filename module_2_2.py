first = int(input('Введите первое чило:'))
second = int(input('Введите второе чило:'))
third = int(input('Введите третье чило:'))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)