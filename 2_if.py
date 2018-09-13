def string_comparison (first_string, second_string):
	if (type(first_string) == str and type(second_string) == str):
		if (first_string == second_string):
			return 1
		elif (len(first_string)>len(second_string)):
			return 2
		elif (second_string=='learn'):
			return 3
	else:
		return 0

# Playing with strings

first_string = 10
second_string = 20
result = string_comparison(first_string, second_string)
print (result)

first_string = "hello"
second_string = "hello"
result = string_comparison(first_string, second_string)
print (result)

first_string = "hello!"
second_string = "world"
result = string_comparison(first_string, second_string)
print (result)

first_string = 'hello'
second_string = 'learn'
result = string_comparison(first_string, second_string)
print (result)

