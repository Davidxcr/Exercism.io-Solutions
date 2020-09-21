def is_armstrong_number(number):
    sum = 0
    length = len(str(number))
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    if number == sum:
        return True
    else:
        return False