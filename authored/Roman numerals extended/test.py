def to_roman_check(roman_digits):
    digits = roman_digits + ['']
    def to_roman2(num):
        roman = ''
        for i in range(len(digits) // 2 - 1, -1, -1):
            digit = num // 10**i
            q, r = divmod(digit, 5)
            if r == 4:
                roman += digits[2 * i] + digits[2 * i + 1 + q]
            else:
                roman += digits[2 * i + 1] * q + digits[2 * i] * r
            num -= digit * 10**i
        return roman
    return to_roman2

from string import ascii_uppercase
from random import randint, shuffle
random = lambda length: randint(1, (4 if length%2 else 9) * 10**((length - 1) // 2) - 1)
to_roman_reduced_check = to_roman_check(['I', 'V', 'X', 'L'])
to_roman_classic_check = to_roman_check(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
to_roman_alphabet_check = to_roman_check(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
to_roman_extended_check = to_roman_check(list(ascii_uppercase))
to_roman_reduced = to_roman(['I', 'V', 'X', 'L'])
to_roman_classic = to_roman(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
to_roman_alphabet = to_roman(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
to_roman_extended = to_roman(list(ascii_uppercase))

test.assert_equals(to_roman_reduced(1), 'I')
test.assert_equals(to_roman_reduced(3), 'III')
test.assert_equals(to_roman_reduced(4), 'IV')
test.assert_equals(to_roman_reduced(58), 'LVIII')
test.assert_equals(to_roman_reduced(89), 'LXXXIX')
test.assert_equals(to_roman_classic(107), 'CVII')
test.assert_equals(to_roman_classic(555), 'DLV')
test.assert_equals(to_roman_classic(496), 'CDXCVI')
test.assert_equals(to_roman_classic(999), 'CMXCIX')
test.assert_equals(to_roman_classic(2021), 'MMXXI')
test.assert_equals(to_roman_alphabet(32), 'CCCAA')
test.assert_equals(to_roman_alphabet(1943), 'GEGCDAAA')
test.assert_equals(to_roman_alphabet(2021), 'GGCCA')
test.assert_equals(to_roman_alphabet(3434), 'GGGEFCCCAB')
test.assert_equals(to_roman_alphabet(3999), 'GGGEGCEAC')
test.assert_equals(to_roman_extended(9876543210), 'SURQQQPOONMLIJGGGEEC')
test.assert_equals(to_roman_extended(1741633356043), 'YXWWUVSRQOOOMMMKKKJHGCDAAA')
test.assert_equals(to_roman_extended(2814235420720), 'YYXWWWUSTQQOOONKLIIFEECC')
test.assert_equals(to_roman_extended(3597684647100), 'YYYXUWTSSRQPOOOMNLKIJHGGE')
test.assert_equals(to_roman_extended(3999999999999), 'YYYWYUWSUQSOQMOKMIKGIEGCEAC')
for i in range(100):
    random_number = random(4)
    test.assert_equals(to_roman_reduced(random_number), to_roman_reduced_check(random_number))
    random_number = random(7)
    test.assert_equals(to_roman_classic(random_number), to_roman_classic_check(random_number))
    random_number = random(7)
    test.assert_equals(to_roman_alphabet(random_number), to_roman_alphabet_check(random_number))
    random_number = random(26)
    test.assert_equals(to_roman_extended(random_number), to_roman_extended_check(random_number))
    random_symbols = list(ascii_uppercase)
    shuffle(random_symbols)
    random_symbols = random_symbols[:randint(1, 26)]
    to_roman_random = to_roman(random_symbols)
    to_roman_random_check = to_roman_check(random_symbols)
    random_number = random(len(random_symbols))
    test.assert_equals(to_roman_random(random_number), to_roman_random_check(random_number))
