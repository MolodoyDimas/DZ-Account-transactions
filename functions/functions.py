import json
from datetime import datetime


def reading_json(json_file):
    '''Получает список '''
    with open(json_file, 'r') as file:
        operations = json.load(file)
        return operations


def mistakes(list):
    '''Удаляет пустые строки и не выполненные операции'''
    good_list = []
    for x in list:
        if len(x) > 0 and x['state'] == "EXECUTED":
            good_list.append(x)
    return good_list


def data_sorting(list):
    '''Сортирует строки по дате и времени от большего к меньшему'''
    list.sort(reverse=True, key=lambda x: x['date'])
    return list


def last_five(list):
    '''Оставляет 5 первых строк'''
    return list[:5]


def hiding_data(name):
    name = name.rsplit(' ', 1)
    if len(name[1]) == 16:
        return f'{name[0]} {name[1][0:4]} {name[1][4:6]}** **** {name[1][12:16]}'
    else:
        return f'{name[0]} **{name[1][-4:]}'


def text_output(list):
    for x in range(len(list)):
        for a in list:
            date_time = datetime.strptime(a["date"], '%Y-%m-%dT%H:%M:%S.%f')
            date = date_time.strftime("%d.%m.%Y")
            if 'from' in a:
                return f'''{date} {a["description"]}
{hiding_data(a["from"])} -> {hiding_data(a["to"])}
{a["operationAmount"]["amount"]} {a["operationAmount"]["currency"]["code"]}'''
            else:
                return f'''{date} {a["description"]}
 -> {hiding_data(a["to"])}
{a["operationAmount"]["amount"]} {a["operationAmount"]["currency"]["code"]}'''


#json_gg = '../tests/output_test.json'
#for x in text_output(reading_json(json_gg)):
#print(text_output(reading_json(json_gg)))
