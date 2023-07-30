from functions import functions
import json
from datetime import datetime
from functions.functions import reading_json

filename = '../data/operations.json'


# list = [{1}, {1}, {1}, {1}]

def test_data_sorting():
    assert functions.data_sorting(
        [{'date': '11.05.2019', '№': '1'}, {'date': '11.05.2013', '№': '2'}, {'date': '11.05.2016', '№': '3'}]) == [
               {'date': '11.05.2019', '№': '1'}, {'date': '11.05.2016', '№': '3'}, {'date': '11.05.2013', '№': '2'}]


def test_last_five():
    assert functions.last_five([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5]
    assert functions.last_five([1, 2, 3]) == [1, 2, 3]


def test_mistakes():
    assert functions.mistakes(
        [{"1": 1, "state": "EXECUTED"}, {"2": 2, "state": "EXECUTED"}, {}, {"3": 3, "state": "CANCELED"}]) == [
               {"1": 1, "state": "EXECUTED"}, {"2": 2, "state": "EXECUTED"}]


def test_reading_json():
    assert functions.reading_json('tests/test_text_to_json.json') == [{"1": 1}, {"2": 2}, {"3": 3}]


def test_hiding_data():
    assert functions.hiding_data("Счет 38976430693692818358") == "Счет **8358"
    assert functions.hiding_data("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"


def test_text_output():
    assert functions.text_output(reading_json('tests/output_test.json')) == '''26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 RUB'''