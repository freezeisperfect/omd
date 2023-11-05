from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    'args, result',
    [
        (
                ['abc', 'abc', 'cba'],
                [('abc', [0, 1]), ('abc', [0, 1]), ('cba', [1, 0])]
        ),
        (
                ['Moscow', 'New York', 'Moscow', 'London'],
                [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]),
                 ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]
        ),
        (
                ['1', '2', '3', '1', '2'],
                [('1', [0, 0, 1]), ('2', [0, 1, 0]), ('3', [1, 0, 0]),
                 ('1', [0, 0, 1]), ('2', [0, 1, 0])]
        )
    ]
)
def test_with_parametrize(args, result):
    assert fit_transform(args) == result


def test_with_assert():
    assert fit_transform('Hello') == [('Hello', [1])]


def test_with_exception():
    with pytest.raises(TypeError):
        fit_transform(123)
    with pytest.raises(TypeError):
        fit_transform(set(1))


@pytest.fixture
def list_to_check():
    return ['amogus', 'aboba', 'aboba', 'cat']


def test_list_to_check(list_to_check):
    assert fit_transform(list_to_check) == [
        ('amogus', [0, 0, 1]),
        ('aboba', [0, 1, 0]),
        ('aboba', [0, 1, 0]),
        ('cat', [1, 0, 0])
    ]
