#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: cclapp
"""

print("Hello, World!!!")

print("No more math.")

print("But I will add some math again")

def area_of_triangle(base, height):
    area = base * height * 0.5
    return area

print(area_of_triangle(10, 2))

a_list = [5, 6, 7, 8, 9]

for i in a_list:
    square = i ** 2
    print(square)

#Creating another function

a_string = "Car"
string_list = ["Car", "House", "Phone"]

def your_wish(x):
    print("I want to buy a " + x)
    
your_wish("Car")

