# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:20:20 2019

@author: aashish
"""

#implement find and replace function
# find() gives the index of first occurence of a character in the string
# replace() replaces all occurences of a char with another char
name=input("Enter a string:")
print(name.find("y"))
print(name.find("b"))
print(name.replace("l", "k"))
print(name.replace("black","blue"))


#Enter a string:sky is black
#2
#7
#sky is bkack
#sky is blue




#swapping  two values
a=input("Enter a:")
b=input("Enter b:")
a,b=b,a
print(a)
print(b)



