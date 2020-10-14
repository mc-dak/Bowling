# -*- coding: utf-8 -*-
import argparse

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>
from bowling_from_to_files import get_score_from_to

parser = argparse.ArgumentParser(description='Script for finding the winner')

if __name__ == "__main__":
    parser.add_argument('--input', action="store", dest="input", required=True)
    parser.add_argument('--output', action="store", dest="output", required=True)
    parser.add_argument('--type', action="store", dest="type", required=True)

args = parser.parse_args()

get_score_from_to(args.input, args.output, args.type)
