"""CTCI problem 1.9."""


def string_rotation(string1, string2):
    """Check if a string is a rotation of another."""
    rotations = []
    for i in range(len(string1)):
        new_rot = string1
        for _ in range(i):
            new_rot += new_rot[0]
            new_rot = new_rot[1:]
        rotations.append(new_rot)

    for rotation in rotations:
        if string2 == rotation:
            return True

    return False
