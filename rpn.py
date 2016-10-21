#!/usr/bin/env python3

import operator, readline
from termcolor import *


operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}

def calculate(myarg):
	printing = myarg.split()
	first = colored(printing[0]+' ', 'blue')
	second = colored(printing[1]+' ', 'blue')
	third = colored(printing[2], 'green')
	if int(printing[0]) < 0:
		first = colored(printing[0]+' ', 'red')
	if int(printing[1]) < 0:
		second = colored(printing[1]+' ', 'red')

	print(first + second + third)
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		cprint(stack, 'yellow')
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def testcoverage():
	cprint('This never runs so coverage should go down', 'red')
	return False

def main():
	while True:
		result = calculate(input("rpn calc> "))
		text = colored('Result: ', 'cyan')
		text2 = colored(str(result), 'cyan')
		print(text + text2)

if __name__ == '__main__':
	main()
