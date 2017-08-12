# -*- coding: utf-8 -*-
#打印下面两行文本，练习\符号，\n, \t, \\
print ("Let's practice everything.")
print ("You\'d need to know \'bout excape with \\ that do \n newlines and \t tabs.")
#给变量名为“诗”的变量赋值，这里是一段文本，所以记住用"""表示，开头和结尾都要有，疑问，如果将"""不单独成行会怎么样？可以，分行是为了美观
poem = """
\tThe lovely world
with logic so firmly planned
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explannation
\n\t\twhere there is none.
"""
#按照下述格式打印上述“诗”的文本
print ("____________________")
print (poem)
print ("____________________")

#给变量five赋值
five = 10 - 2 + 3 - 6
#打印下述文本，含%s格式符，指代字符串变量，%d指代数值变量，%r指代一切原始输入
print ("This should be five: %s" % five)
#定义函数secret_formula，含started一个变量
def secret_formula (started):
	#在这个函数里，jelly_beans这个变量的值永远等于started变量的值乘以500，练习数学算式
	jelly_beans = started * 500
	#同上
	jars = jelly_beans / 1000
	crates = jars / 100
	#必须返回函数的值，这里将返回三个新计算的变量的值
	return jelly_beans, jars, crates
#指定变量start_point的值为10000
start_point = 10000
#调用函数secret_formula，对beans, jars, crates赋值
beans, jars, crates = secret_formula (start_point)
#打印下面文本，练习以%d指代单个变量的数值
print ("With a starting point of %d" % start_point)
#打印下面文本，练习以%d指代多个变量的数值
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
#对start_point重新赋值，在原start_point值的基础上缩小10倍
start_point = start_point / 10
#打印
print ("We can also do that this way.")
#打印，对变量的赋值通过调用函数计算而得
print ("We'd have %d beans, %d jars, %d crates" % secret_formula (start_point))