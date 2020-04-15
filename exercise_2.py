import pytest


class TestRomanNumeralConverter:

    def test_convert_0(self):
        self._test_convert_helper(input=0, expected_result="nulla")

    def _test_convert_helper(self, input, expected_result):
        result = RomanNumeralConverter.convert(input)

        assert expected_result == result

    def test_convert_1(self):
        self._test_convert_helper(input=1, expected_result="I")

    def test_convert_all_values(self):
        self._test_convert_helper(input=2, expected_result="II")
        self._test_convert_helper(input=3, expected_result="III")
        self._test_convert_helper(input=4, expected_result="IV")
        self._test_convert_helper(input=5, expected_result="V")
        self._test_convert_helper(input=10, expected_result="X")
        self._test_convert_helper(input=50, expected_result="L")

    def test_convert_number_over_3999(self):
        with pytest.raises(AboveMaxRomanNumeralConverterException):
            RomanNumeralConverter.convert(4000)

    def test_convert_max(self):
        self._test_convert_helper(input=3999, expected_result="MMMCMXCIX")

    def test_convert_numbers(self):
        self._test_convert_helper(input=3111, expected_result="MMMCXI")
        self._test_convert_helper(input=300, expected_result="CCC")
        self._test_convert_helper(input=20, expected_result="XX")


class RomanNumeralConverter:
    NULLA = "nulla"
    MAX_NUMBER = 3999
    CONVERTER_MAP = {
        0: NULLA,
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    @classmethod
    def convert(cls, number):
        if number > cls.MAX_NUMBER:
            raise AboveMaxRomanNumeralConverterException
        try:
            return cls.CONVERTER_MAP[number]
        except KeyError:
            return cls._convert_numbers_not_in_map(number)

    @classmethod
    def _convert_numbers_not_in_map(cls, number):
        roman_numeral_result = ""
        for arabic_number, roman_number in cls._get_roman_numerals_in_reverse():
            if number == 0:
                return roman_numeral_result
            if arabic_number <= number:
                mod_remainder = number % arabic_number
                factor = int((number - mod_remainder)/arabic_number)
                roman_numeral_result += factor * roman_number
                number = mod_remainder

    @classmethod
    def _get_roman_numerals_in_reverse(cls):
        numbers_list = list(cls.CONVERTER_MAP.items())
        numbers_list.reverse()
        return numbers_list

class AboveMaxRomanNumeralConverterException(Exception):

    def __init__(self):
        self.message = "Only numbers up to 3999 are suppported"