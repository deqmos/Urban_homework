def get_multiplied_digits(number):
    if number == 0:
        return 1
    elif number % 10 == 0:
        return get_multiplied_digits(number // 10)
    else:
        return (number % 10) * get_multiplied_digits(number // 10)


result = get_multiplied_digits(40203)
print(result)
