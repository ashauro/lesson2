dic = {"Как дела?": "Хорошо!", "Что делаешь?": "Ем людей", 'Что ты хочешь?':'Твою душу!'}

def ask_user (dic):
	while True :
		found_result = False
		q  = input ('Пожалуйста, задайте вопрос: ')
		if q == 'Пока!':
			print ('До скорой встречи!')
			break
		for question, answer in dic.items():
			if q == question:
				print(answer)
				found_result = True
		if found_result == False:
			print ('Я не знаю ответа на Ваш вопрос :(')

ask_user(dic)