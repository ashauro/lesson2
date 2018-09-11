score_list = [
	{'school_class' : '1a', 'scores':[4,4,2,2,5]},
	{'school_class' : '1b', 'scores':[2,2,3,5,5]},
	{'school_class' : '1c', 'scores':[5,5,5,3,4]}
	]

current_score = 0
sum_of_scores = 0
number_of_scores = 0
class_number = 0

for main_data_string in score_list:
	class_number = main_data_string.get('school_class')
	score_string = main_data_string.get('scores')

	for current_score in score_string:
		sum_of_scores = sum_of_scores + current_score
		number_of_scores = number_of_scores + 1
	
	print ('Список оценок класса {} - {}'.format(class_number, score_string))
	print ('Средний балл {} класса составляет: {}'.format(class_number, round(sum_of_scores/number_of_scores,2)))

average_score = sum_of_scores/number_of_scores

print ('Сумма баллов по всем классам составляет: {}'.format(sum_of_scores))	
print ('Всего оценок: {}'.format(number_of_scores))
print ('Средний балл: {}'.format(round(average_score,2)))	


