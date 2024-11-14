from random import randint
number = randint(3,20)
print(f'Число для пароля: {number}')
result = ''
for i in range(1, number + 1):
    for j in range(i, number + 1):
        if i == j:
            continue
        if number % (i + j) == 0 :
            result = result+str(i)+str(j)
print(f'Пароль: {result}')