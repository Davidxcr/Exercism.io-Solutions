enter_name = str(input("Please enter a name: "))

def two_fer():
    if enter_name == "":
        return 'One for me, one for you'

    else:
        return'One for " + enter_name + ", one for me"'

two_fer()