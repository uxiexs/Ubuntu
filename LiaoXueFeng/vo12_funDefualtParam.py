#/usr/bin/python3
# coding:utf-8
name = input("Please input your name: ")
gender = input("Plaese input your gender: ")


def enroll(name, gender, age=6, city='Beijing'):
    return {'name': name, 'gender': gender, 'age': age, 'city': city}

print(enroll(name, gender))
