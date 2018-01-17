"""Boggle words."""


def boggle_words(input_matrix):
    """Return all of the words in the input matrix."""
    words = set()

    rows = len(input_matrix)
    cols = len(input_matrix[0])

    for i in rows:
        for j in cols:
            # BFS
            pot_words = [input_matrix[i][j]]
            while pot_words:

                current_word = pot_words.pop(0)

                if is_word(current_word):
                    words.add(current_word)

                neighbors = [(i + a[0], j + a[1]) for a in [(0, 1), (0, -1), (1, 0), (-1, 0)] if input_matrix[i + a[0]][j + a[1]]]

                for neighbor in neighbors:
                    pot_words.append(current_word + input_matrix[neighbor[0]][neighbor[1]])

    return words
