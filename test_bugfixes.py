"""
Tests for Exercise 6: Finding & Fixing Bugs
Run with: python -m pytest test_bugfixes.py -v
"""
import pytest
from buggy_code import (
    sum_range,
    is_valid_age,
    get_first_word,
    find_min_max,
    can_ride_rollercoaster,
    find_index,
    get_grade_letter,
    count_vowels,
    remove_duplicates,
    calculate_discount,
)


class TestBug1_OffByOne:
    def test_sum_1_to_5(self):
        assert sum_range(1, 5) == 15, "1+2+3+4+5 = 15"

    def test_sum_same_number(self):
        assert sum_range(3, 3) == 3, "3 to 3 inclusive should be 3"

    def test_sum_1_to_1(self):
        assert sum_range(1, 1) == 1


class TestBug2_WrongOperator:
    def test_valid_age(self):
        assert is_valid_age(25) == True

    def test_age_zero_valid(self):
        assert is_valid_age(0) == True, "0 should be valid"

    def test_age_150_valid(self):
        assert is_valid_age(150) == True, "150 should be valid"

    def test_negative_invalid(self):
        assert is_valid_age(-1) == False

    def test_151_invalid(self):
        assert is_valid_age(151) == False


class TestBug3_NullCheck:
    def test_normal_sentence(self):
        assert get_first_word("Hello world") == "Hello"

    def test_single_word(self):
        assert get_first_word("Python") == "Python"

    def test_empty_string(self):
        assert get_first_word("") == ""

    def test_none(self):
        assert get_first_word(None) == ""


class TestBug4_WrongReturn:
    def test_basic(self):
        assert find_min_max([3, 1, 4, 1, 5]) == (1, 5)

    def test_single(self):
        assert find_min_max([7]) == (7, 7)

    def test_negative(self):
        assert find_min_max([-3, -1, -4]) == (-4, -1)


class TestBug5_Logic:
    def test_tall_and_old(self):
        assert can_ride_rollercoaster(130, 10, False) == True

    def test_tall_and_consent(self):
        assert can_ride_rollercoaster(130, 5, True) == True

    def test_too_short(self):
        assert can_ride_rollercoaster(110, 10, False) == False

    def test_too_short_with_consent(self):
        assert can_ride_rollercoaster(110, 5, True) == False, \
            "Parent consent shouldn't override height requirement"


class TestBug6_InfiniteLoop:
    def test_found(self):
        assert find_index(["a", "b", "c"], "b") == 1

    def test_not_found(self):
        assert find_index(["a", "b", "c"], "d") == -1

    def test_empty(self):
        assert find_index([], "a") == -1

    def test_first(self):
        assert find_index(["x", "y"], "x") == 0


class TestBug7_GradeLetter:
    def test_a(self):
        assert get_grade_letter(95) == "A"

    def test_b(self):
        assert get_grade_letter(85) == "B"

    def test_c(self):
        assert get_grade_letter(75) == "C"

    def test_d(self):
        assert get_grade_letter(65) == "D"

    def test_f(self):
        assert get_grade_letter(42) == "F"

    def test_exactly_80(self):
        assert get_grade_letter(80) == "B"

    def test_exactly_90(self):
        assert get_grade_letter(90) == "A"


class TestBug8_CaseInsensitive:
    def test_mixed_case(self):
        assert count_vowels("Hello World") == 3

    def test_uppercase(self):
        assert count_vowels("PYTHON") == 1, "Y is not a vowel, O is"

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_all_uppercase_vowels(self):
        assert count_vowels("AEIOU") == 5


class TestBug9_ListMutation:
    def test_basic(self):
        assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

    def test_strings(self):
        assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]

    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_all_same(self):
        assert remove_duplicates([5, 5, 5]) == [5]


class TestBug10_Calculation:
    def test_20_percent_off(self):
        assert calculate_discount(100, 20) == 80.0

    def test_10_percent_off(self):
        assert calculate_discount(50, 10) == 45.0

    def test_no_discount(self):
        assert calculate_discount(200, 0) == 200.0

    def test_50_percent_off(self):
        assert calculate_discount(100, 50) == 50.0
