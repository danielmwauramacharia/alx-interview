#!/usr/bin/python3
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

    # # This was my solution
    # if not isinstance(n, int):
    #     raise TypeError("n should be an integer")
    # mainlist = []
    # if n <= 0:
    #     return mainlist
    # if n == 1:
    #     mainlist.append([1])
    #     return mainlist
    # if n > 2:
    #     mainlist.append([1])
    #     mainlist.append([1, 1])
    # if n == 2:
    #     return mainlist
    # x = 3
    # while x <= n:
    #     new = []
    #     val = x - 2
    #     wrklist = mainlist[val]
    #     for i in range(val):
    #         val1 = wrklist[i]
    #         val2 = wrklist[i + 1]
    #         value = val1 + val2
    #         new.append(value)
    #     new.insert(0, 1)
    #     new.append(1)
    #     x += 1
    #     mainlist.append(new)
    # return mainlist

    # below is the solution after research
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[j] + prev_row[j + 1]
                         for j in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)
    return triangle
