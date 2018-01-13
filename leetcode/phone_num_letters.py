"""Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


def phone_num_letters(number_sequence):
    """Determine all possible letter combos."""
    num_letters = {
                    '1': [],
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f']
                   }

    letter_combos = []
    possible_string = ''
    count = 0

    def find_combos(count, possible_string):
        """."""
        if len(number_sequence) - 1 < count:
            letter_combos.append(possible_string)
            return

        num = number_sequence[count]
        for letter in num_letters[num]:
            find_combos(count + 1, possible_string + letter)

    find_combos(count, possible_string)

    return letter_combos
