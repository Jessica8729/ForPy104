# -*- coding: utf-8 -*-
#定义加函数，2个变量
def add (a, b):
	#输出由a, b两变量构成的加函数公式
	print ("ADDING %d + %d" % (a, b))
	#返回加函数的值，函数中一定要有return返回值才是完整的函数
	return a + b
#定义减函数，2个变量
def subtract (a, b):
	#输出减函数的公式
	print ("SUBTRACTING %d - %d" % (a, b))
	#返回减函数的值
	return a - b

def multiply (a, b):
	print ("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide (a, b):
	print ("DIVIDING %d / %d" % (a, b))
	return a / b

#输出这句话
print ("Let's do some math with just functions!")
#调用加减乘除函数，分别列出四个变量的计算公式
age = add (30, 5)
height = subtract (78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)
#一行输出四个变量的值
print ("age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


#A puzzle for the extra credit, type it in anyway
print ("Here is a puzzle.")
#做个比较复杂的计算，同时调用加减乘除四个函数，为变量what赋值
what = add (age, subtract (height, multiply (weight, divide (iq, 2))))
#输出这个数字游戏的计算值
print ('That becomes', what, 'Can you do it by hand?')
