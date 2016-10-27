age = input('Please enter your age:')


def ageFun(age):
    age = int(age)
    if 0<=age<18:
        print("you're age is",age)
        print("greenager")
        quit
    elif 18<=age<60:
        print("you're age is", age)
        print("adult")
        quit
    elif 60<=age<150:
        print("you're age is",age)
        print("oldman")
        quit
    else:
        print('monster')
        quit
ageFun(age)
