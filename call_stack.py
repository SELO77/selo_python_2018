import inspect


def list_num(num, result=0):
	if num == 0:
		return result
	result *= 10
	result += num
	print(len(inspect.stack()))
	return list_num(num-1, result)


if __name__ == '__main__':
	print("START")
	num = int(input("Input Positive Integer"))
	result = list_num(num)
	print(result)
