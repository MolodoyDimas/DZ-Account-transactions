import json
from functions.functions import reading_json, hiding_data, text_output, mistakes, last_five, data_sorting


# Путь к нужному файлу
filename = 'data/operations.json'

#Делаем подряд всё нужное для подготовки информации. P.s. не знаю как правильней это написать, поочереди или в одну строку разом.
ready_lines = reading_json(filename)
ready_lines = mistakes(ready_lines)
ready_lines = data_sorting(ready_lines)
ready_lines = last_five(ready_lines)

# Выводим информацию подряд
for x in ready_lines:
    print(f'{text_output([x])}\n')
