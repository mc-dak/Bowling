# -*- coding: utf-8 -*-
import re


def get_score(result, counting_type):
    try:
        general_check(result)
        counting_type_check(counting_type)

        previous_char = None
        prev_prev_char = None
        number_in_frame = 1
        previous_digit_to_sum = 0
        digit_to_sum = 0
        total = 0

        for char in result:
            sequence_check(char, previous_digit_to_sum, number_in_frame, previous_char)

            if counting_type == 'internal':
                digit_to_sum = internal_condition(char, previous_digit_to_sum)
            elif counting_type == 'external':
                digit_to_sum = external_condition(char, previous_digit_to_sum)
                bonus = bonus_condition(char, prev_prev_char, previous_char)
                total += bonus
                prev_prev_char = previous_char

            total += digit_to_sum
            previous_digit_to_sum = digit_to_sum
            previous_char = char

            if char != 'X':
                number_in_frame += 1
            if char == 'X' or number_in_frame == 3:
                number_in_frame = 1
        print('Количество очков для результатов ' + result + ' - ' + str(total))
        return total
    except TypeError as ex:
        print(ex)


def sequence_check(char, previous_digit_to_sum, number_in_frame, previous_char):
    if number_in_frame == 1 and char == '/':
        raise TypeError('Содержится недопустимая последовательность символов, / на первом месте фрейма')
    if previous_char == '-' and number_in_frame == 2 and \
            char == 'X':
        raise TypeError('Содержится недопустимая последовательность символов, -X')
    if number_in_frame == 2 and char == 'X' and re.search(r'[^/X-]', str(previous_char)):
        raise TypeError('Содержится недопустимая последовательность символов, dX')
    if number_in_frame == 2 and re.search(r'[^/X-]', str(previous_char)) and \
            re.search(r'[^/X-]', str(char)) and (previous_digit_to_sum + int(char)) >= 10:
        raise TypeError('Содержится недопустимая последовательность символов, сумма во фрейме не может быть '
                        'больше 9 за исключением X и /')


def general_check(result):
    if not isinstance(result, str):
        raise TypeError('Входящие данные не str')
    if re.search(r'[^/\dX-]', result):
        raise TypeError('Содержатся недопустимые символы')
    symbol_x = '(?=(%s))' % re.escape('X')
    count_strikes = len(re.findall(symbol_x, result))
    count_aim = 20 - count_strikes
    if len(result) != count_aim:
        raise TypeError('Неверное количество бросков для полноценной игры')


def counting_type_check(counting_type):
    if counting_type not in ['internal', 'external']:
        raise TypeError("Неправильное значение типа подсчета очков, должно быть или 'internal' или "
                        "'external' ")


def internal_condition(char, previous_digit_to_sum):
    elem = 0
    if char == 'X':
        elem = 20
    elif char == '/':
        elem = 15 - previous_digit_to_sum
    elif char == '-':
        elem = 0
    elif int(char):
        elem = int(char)
    return elem


def external_condition(char, previous_digit_to_sum):
    elem = 0
    if char == 'X':
        elem = 10
    elif char == '/':
        elem = 10 - previous_digit_to_sum
    elif char == '-':
        elem = 0
    elif int(char):
        elem = int(char)
    return elem


def bonus_condition(char, prev_prev_char, previous_char):
    bonus1 = 0
    bonus2 = 0
    if previous_char == '/' and re.search(r'[^/X-]', str(char)):
        bonus1 = int(char)
    if previous_char == '/' and char == 'X':
        bonus1 = 10
    if previous_char == 'X' and re.search(r'[^/X-]', str(char)):
        bonus1 = int(char)
    if previous_char == 'X' and char == 'X':
        bonus1 = 10
    if prev_prev_char == 'X' and re.search(r'[^/X-]', str(char)):
        bonus2 = int(char)
    if prev_prev_char == 'X' and char == 'X':
        bonus2 = 10
    bonus = bonus1 + bonus2
    return bonus
