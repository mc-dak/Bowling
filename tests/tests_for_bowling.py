import unittest
from bowling import get_score
from bowling import general_check
from bowling import counting_type_check
from bowling import sequence_check


class BowlingTest(unittest.TestCase):

    def test_count_scores_internal(self):
        result = get_score('XXX347/X1212X13', 'internal')
        self.assertEqual(result, 132)

    def test_count_scores_external(self):
        result = get_score('XXX347/X1212X13', 'external')
        self.assertEqual(result, 134)

    def test_not_string(self):
        with self.assertRaises(TypeError) as error:
            general_check([])
        self.assertEqual(f"{error.exception}", 'Входящие данные не str')

    def test_not_right_count_of_aims(self):
        with self.assertRaises(TypeError) as error:
            general_check('X/--/-54--XX-/-6')
        self.assertEqual(f"{error.exception}", 'Неверное количество бросков для полноценной игры')

    def test_unacceptable_symbols(self):
        with self.assertRaises(TypeError) as error:
            general_check('XYX347/X1212X13')
        self.assertEqual(f"{error.exception}", 'Содержатся недопустимые символы')

    def test_error_in_counting_type(self):
        with self.assertRaises(TypeError) as error:
            counting_type_check('intern')
        self.assertEqual(f"{error.exception}", "Неправильное значение типа подсчета очков, должно быть или 'internal' "
                                               "или 'external' ")

    def test_unacceptable_sequence_var1(self):
        """
        'X/----/-54---XX/-16'
        """
        char = '/'
        previous_elem = None
        number_in_frame = 1
        previous_char = 'X'
        with self.assertRaises(TypeError) as error:
            sequence_check(char, previous_elem, number_in_frame, previous_char)
        self.assertEqual(f"{error.exception}", 'Содержится недопустимая последовательность символов, / на первом месте '
                                               'фрейма')

    def test_unacceptable_sequence_var2(self):
        """
        '-/-X-/-54--XX-/-6'
        """
        char = 'X'
        previous_elem = None
        number_in_frame = 2
        previous_char = '-'
        with self.assertRaises(TypeError) as error:
            sequence_check(char, previous_elem, number_in_frame, previous_char)
        self.assertEqual(f"{error.exception}", 'Содержится недопустимая последовательность символов, -X')

    def test_unacceptable_sequence_var3(self):
        """
        '1772-/X2X1-XXX-'
        """
        char = 'X'
        previous_elem = None
        number_in_frame = 2
        previous_char = '5'
        with self.assertRaises(TypeError) as error:
            sequence_check(char, previous_elem, number_in_frame, previous_char)
        self.assertEqual(f"{error.exception}", 'Содержится недопустимая последовательность символов, dX')

    def test_unacceptable_sequence_var4(self):
        """
        '-/X---/--56XX-/-6'
        """
        char = '6'
        previous_elem = 5
        number_in_frame = 2
        previous_char = '5'
        with self.assertRaises(TypeError) as error:
            sequence_check(char, previous_elem, number_in_frame, previous_char)
        self.assertEqual(f"{error.exception}",
                         'Содержится недопустимая последовательность символов, сумма во фрейме не может быть '
                         'больше 9 за исключением X и /')
