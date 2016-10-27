#/usr/bin/python3
#coding:utf-8
def getBmi(bmi):
    print('BMI:',bmi)
    if bmi<18.5:
        print ("too light")
        quit
    elif 18.5<=bmi<25:
        print("normal")
        quit
    elif 25<=bmi<28:
        print( "too heavy")
        quit
    elif 28<=bmi<32:
        print("fat")
        quit
    else:
        print("too fat")
        quit

height = input("Please enter you're height:")
weight = input("Please enter you're weight:")
bmi = int(weight)/(float(height)**2)
getBmi(bmi)
