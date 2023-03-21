import pytest
from arrays import add


def test_add():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expect = [5, 7, 9]

    output = add(a, b)

    assert output == expect


def test_add_arrays1():
    a = [-1, -5, -3]
    b = [-4, -3, 0]
    expect = [-5, -8, -3]

    output = add(a, b)

    assert output == expect


@pytest.mark.parametrize(
        "a, b, expect", [
            ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
            ([-1, -5, -3], [-4, -3, 0], [-5, -8, -3]),
        ]
)
def test_add_arrays(a, b, expect):
    output = add(a, b)

    assert output == expect


def test_add_arrays_error():
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        add(a, b)
