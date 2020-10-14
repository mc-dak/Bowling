# -*- coding: utf-8 -*-
from bowling import get_score


def get_score_from_to(input_file, output_file, count_type):
    substring1 = '###'
    substring2 = 'winner is '

    # with open(input_file, 'r', encoding='utf-8') as file, open(output_file, 'w') as writefile:
    with open(input_file, 'r') as file, open(output_file, 'w') as writefile:
        for line in file:
            try:
                if substring1 in line:
                    max_number = 0
                    writefile.write(line)
                elif substring2 in line:
                    writefile.write(substring2 + '' + winner_name + '\n')
                else:
                    name, result = line.split(' ')
                    result = result.strip()
                    count = get_score(result, count_type)
                    writefile.write(line.strip() + ' ' + str(count) + '\n')
                    if count > max_number:
                        max_number = count
                        winner_name = name
            except Exception as exc:
                print('error', exc, line)


file1 = 'tournament.txt'
file2 = 'tournament_result.txt'
counting_type = 'internal'
# counting_type = 'external'

get_score_from_to(file1, file2, counting_type)
