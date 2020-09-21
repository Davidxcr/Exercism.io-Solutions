def is_armstrong_number(number):
    sum = 0     #initialize sum
    length = len(str(number)) #initialize length of number
    temp = number   #set temp to numer

    while temp > 0:
        digit = temp % 10   #modulo of number will be last digit of number
        sum += digit ** length  #add last digit to the answer and divide each by length
        temp //= 10     #number divided by 10

    if number == sum:
        return True
    else:
        return False