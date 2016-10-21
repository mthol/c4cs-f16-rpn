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
		cprint(stack, 'red')
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
