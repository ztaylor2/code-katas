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


from given import get_words


NEIGHBORS = [(-1, -1), (0, -1), (1, -1),
             (-1, 0),           (1, 0),
             (-1, 1), (0, 1),   (1, 1)]

# alternate solution
def solve(grid):
    """Find all words on the grid."""
    results = []
    words = set(word for words in get_words() if len(word) >= 3)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            results += find_words(grid, words, grid[y][x], y, x, set([y, x]))
    return set(results)


def find_words(grid, words, current, y, x, used):
    """Find the words with DFS."""
    found = []
    if current in words:
        found.append(current)
    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
    if in_grid(grid, ny, nx) and (ny, nx) not in used:
        used.add((ny, nx))
        found.extend(find_words(grid, words, current+grid[ny][nx], ny, nx, used))
        used.remove((nx, ny))

def in_grid(grid, y, x):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])

grid = 
