def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1 and str_number != '0':
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    elif str_number == '0':
        return 1
    else:
        return first



result = get_multiplied_digits(402030)

print(result)

