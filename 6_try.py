def get_summ (num_one, num_two):
	try:
		int_num_one = int(num_one)
		int_num_two = int(num_two)
		print (int_num_one + int_num_two)
	except ValueError:
		print ('Вы ввели не целое число(а)!')


num_one = input ('Введите ЦЕЛОЕ первое число: ')
num_two = input ('Введите ЦЕЛОЕ второе число: ')
get_summ (num_one, num_two)