"""You have to build a pyramid.

This pyramid should be built from characters from a given string.

You have to create the code for these four methods:

watch_pyramid_from_the_side(characters):

watch_pyramid_from_above(characters):

count_visible_characters_of_the_pyramid(characters):

count_all_characters_of_the_pyramid(characters):
The first method ("FromTheSide") shows the pyramid as you would see from the side.
The second method ("FromAbove") shows the pyramid as you would see from above.
The third method ("CountVisibleCharacters") should return the count of all characters, that are visible from outside the pyramid.
The forth method ("CountAllCharacters") should count all characters of the pyramid. Consider that the pyramid is completely solid and has no holes or rooms in it.

Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.
The pyramid should have perfect angles of 45 degrees.


Example: Given string: "abc"

Pyramid from the side:

  c
 bbb
aaaaa
Pyramid from above:

aaaaa
abbba
abcba
abbba
aaaaa
Count of visible stones/characters:

25
Count of all used stones/characters:

35

There is no meaning in the order or the choice of the characters. It should work the same for example "aaaaa" or "54321". 
Hint: Your output for the side must always be a rectangle! So spaces at the end of a line must not be deleted or trimmed! 
If the string is null or empty, you should exactly return this value for the watch-methods and -1 for the count-methods. ."""


def pyramid(characters):
    """."""
    # I solved it backwords
    characters[::-1]

    depth = len(characters)
    letter_line = depth + (depth - 1)
    first_poss = int((letter_line / 2) + .5)

    pos_to_print_letter = [first_poss]

    for x, letter in enumerate(characters):
        line = ''
        for i in range(letter_line):
            if i in pos_to_print_letter:
                    line += letter
            else:
                line += ' '
        print(line)
        pos_to_print_letter = [pos_to_print_letter[0] - 1] + pos_to_print_letter + [pos_to_print_letter[-1] + 1]
if __name__ == '__main__':
    pyramid('abc')
