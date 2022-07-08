def divisor(n1):
	def dividend(n2):
		return n2/n1
	return dividend

def execute():
	division_by_3 = divisor(3)
	print(division_by_3(18))
	division_by_5 = divisor(5)
	print(division_by_5(100))
	division_by_18 = divisor(18)
	print(division_by_18(54))

if __name__ == '__main__':
	execute() 