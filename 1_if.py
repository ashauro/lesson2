
import sys

def type_of_activity (user_age):
	try:
		user_age=int(user_age)
		if user_age <= 6:
			return 'Ути-пути!'
		elif user_age >6 and user_age<=17:
			return 'Ученье свет!'
		elif user_age >17 and user_age<=23:
			return 'Мам, мне ко второй!'
		elif user_age >24 and user_age<100:
			return 'Arbeit macht frei!'
		else:
			return 'А вы точно еще живы?'
	except (TypeError, ValueError):
		print("Неверный тип данных")
		sys.exit ()

user_age = input ('Пожалуйста, введите свой возраст: ')
user_activity =  type_of_activity(user_age)
print (user_activity)
