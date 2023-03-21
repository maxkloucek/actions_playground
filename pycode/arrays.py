# https://milliams.com/courses/software_engineering_best_practices/Testing.html
# using UoB ACRC https://www.bristol.ac.uk/acrc/acrc-training/ course to test
# automating unit testing with github actions


def add(x, y):
    """
    This function performs element wise addtion for two lists

    Args:
        x (list): First list
        y (list): Second list

    Returns:
        list: pairwise sums of elements ``x`` and ``y``.

    Raises:
        ValueError: If len(x) != len(y)

    Examples:
        >>> add([1, 2], [3, 4])
        [4, 6]
    """
    if len(x) != len(y):
        raise ValueError(
            f"Lengths of lists must match. x is {len(x)} long, y is {len(y)}")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ + y_)
    return z
