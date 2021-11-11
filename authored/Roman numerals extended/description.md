### Task

The [roman numeral system](https://en.wikipedia.org/wiki/Roman_numerals) uses the letters `['I','V','X','L','C','D','M']` to represent numbers from `1` up to `3999`.
A converter function takes in a decimal number and translates it to a roman numeral. Your task is to create a function that takes in an array of symbols and returns a converter for that array.

### Examples

```
to_roman_classic = to_roman(['I', 'V', 'X', 'L', 'C', 'D', 'M'])
to_roman_classic(2021)
# returns: 'MMXXI'

to_roman_reduced = to_roman(['I', 'V', 'X', 'L'])
to_roman_reduced(89)
# returns: 'LXXXIX'

to_roman_alphabet = to_roman(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
to_roman_alphabet(2021)
# returns: 'GGCCA'

to_roman_extended = to_roman(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
to_roman_extended(9876543210)
# returns: 'SURQQQPOONMLIJGGGEEC'
```

### Input

An array of uppercase letter of the english alphabet.
The value of the symbol in the array (0-indexed) at index `i` is:

- if `i` is even: `10**(i / 2)`
- if `i` is odd: `10**((i - 1) / 2) * 5`

### Constraints

- the number tested are always representable with the given array of symbols
- the number tested are positive integers under 9e12
- the symbols are upper case letters of the english alphabet
- the length of the array of symbols is between 1 and 26
