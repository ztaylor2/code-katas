"""Boggle words."""

# from given import get_words


# NEIGHBORS = [(-1, -1), (0, -1), (1, -1),
#              (-1, 0),           (1, 0),
#              (-1, 1), (0, 1),   (1, 1)]


# def solve(grid):
#     """Find all words on the grid."""
#     results = []
#     words = set(word for word in get_words() if len(word) >= 3)
#     for y in range(len(grid)):
#         for x in range(len(grid[y])):
#             results += find_words(grid, words, grid[y][x], y, x, set([y, x]))
#     return set(results)


# def in_grid(grid, y, x):
#     """."""
#     return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y])


# def find_words(grid, words, current, y, x, used):
#     """Find the words with DFS."""
#     found = []
#     if current in words:
#         found.append(current)
#     for dx, dy in NEIGHBORS:
#         nx, ny = x + dx, y + dy
#         if in_grid(grid, ny, nx) and (ny, nx) not in used:
#             used.add((ny, nx))
#             found.extend(find_words(grid, words, current+grid[ny][nx], ny, nx, used))
#             used.remove((nx, ny))
#     return found
