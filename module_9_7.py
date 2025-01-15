def is_prime(func):
    def wrapper(*args):
        prime = True
        result = func(*args)
        if result > 1:
            for j in range(2, result):
                if result % j == 0:
                    prime = False
                    break
            if prime:
                print('Простое')
            else:
                print('Составное')
            return result
        else:
            return 'Число меньше или равно единице'
    return wrapper

@is_prime
def sum_three(*args):
    d = 0
    for i in args:
        d+= i
    return d

result = sum_three(1,2,3,4,5,6,7,8,1)
print(result)