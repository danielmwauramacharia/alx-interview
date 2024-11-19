"""
working on Pascal Triangle Interview Question
"""


def pascal_triangle(n):
    """
    Function that returns lists of lists of Intergers.

    The list represent the pascal triangle.

    Args:
        n (Integer): The integer should be positive and > than zero.
    """

    if not isinstance(n, int):
        raise TypeError("n should be an integer")
    mainlist = []
    if n <= 0:
        return mainlist
    if n == 1:
        mainlist.append([1])
        return mainlist
    if n > 2:
        mainlist.append([1])
        mainlist.append([1, 1])
    if n == 2:
        return mainlist
    x = 3
    while x <= n:
        new = []
        val = x - 2
        wrklist = mainlist[val]
        for i in range(val):
            val1 = wrklist[i]
            val2 = wrklist[i + 1]
            value = val1 + val2
            new.append(value)
        new.insert(0, 1)
        new.append(1)
        x += 1
        mainlist.append(new)
    return mainlist
