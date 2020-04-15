# Implement a class that checks if a year is a leap year

# All the following rules must be satisfied:

# Is NOT a leap year if NOT divisible by 4
# Is a leap year if divisible by 4
# Is a leap year if divisible by 400
# Is NOT a leap year if divisible by 100 but NOT by 400
# Examples:

# 1997 is NOT a leap year (not divisible by 4)
# 1996 is a leap year (divisible by 4)
# 1600 is a leap year (divisible by 400)
# 1800 is NOT a leap year (divisible by 4, divisible by 100, NOT divisible by 400)

class TestYear:

    def test_is_leap_year_given_not_divisible_by_4_return_false(self):
        result = Year(1997).is_leap_year()

        assert result == False

    def test_is_leap_year_given_divisible_by_4_return_true(self):
        result = Year(1996).is_leap_year()

        assert result == True

    def test_is_leap_year_given_divisible_by_400_return_true(self):
        result = Year(1600).is_leap_year()

        assert result == True

    def test_is_leap_year_given_divisible_by_100_and_not_400_return_false(self):
        result = Year(1800).is_leap_year()

        assert result == False

class Year:

    def __init__(self, year):
        self.year = year
    
    def is_leap_year(self):
        return self._is_divisible_by(4) and not (self._is_divisible_by(100) and not self._is_divisible_by(400))

    def _is_divisible_by(self, number):
        return self.year % number == 0