"""
One hot encoding test
"""
import pytest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_fit_transform_result_1():
    actual = fit_transform(['ANALYSIS', 'PHYSICS', 'TOPOLOGY'])
    expected = [
        ('ANALYSIS', [0, 0, 1]),
        ('PHYSICS', [0, 1, 0]),
        ('TOPOLOGY', [1, 0, 0]),
    ]

    assert actual == expected


def test_fit_transform_result_1():
    actual = fit_transform(['Cat', 'Dog', 'Cat', 'Cow'])
    expected = [
        ('Cat', [0, 0, 1]),
        ('Dog', [0, 1, 0]),
        ('Cat', [0, 0, 1]),
        ('Cow', [1, 0, 0]),
    ]

    assert actual == expected


def test_fit_transform_other_word():
    actual = ['ANALYSIS', 'PHYSICS', 'TOPOLOGY', 'STATISTICS']
    other_word = 'HISTORY'
    transformed_cities = fit_transform(actual)

    for val, transformed_val in transformed_cities:
        assert other_word not in val


def test_exception():
    actual = fit_transform(['One', 'Two', 'Three'])

    with pytest.raises(TypeError):
        print(actual / 5)


if __name__ == '__main__':
    pass
