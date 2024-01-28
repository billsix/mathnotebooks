from billsixmathnotebooks.prealgebra.utils import (
    _add_decimals_split_decimals,
    _add_decimals_actually_add_them,
    _subtract_decimals_split_decimals,
    _subtract_decimals_put_zeros_on_end,
    _subtract_decimals_split_decimals2,
    _subtract_decimals_actually_subtract_them,
    _add_decimals_put_zeros_on_end,
)


def test_add_decimals_split_decimals():
    assert (("1", "2"), ("3", "4")) == _add_decimals_split_decimals(first="1.2", second="3.4")


def test_add_decimals_put_zeros_on_end():
    assert ("120", "345") == _add_decimals_put_zeros_on_end(first_dec="12", second_dec="345")
    assert ("120000", "345678") == _add_decimals_put_zeros_on_end(first_dec="12", second_dec="345678")
    assert ("125", "340") == _add_decimals_put_zeros_on_end(first_dec="125", second_dec="34")
    assert ("125678", "340000") == _add_decimals_put_zeros_on_end(first_dec="125678", second_dec="34")


def test_add_decimals_actually_add_them():
    assert ("4", "6") == _add_decimals_actually_add_them(
        first_whole="1", first_dec="2", second_whole="3", second_dec="4"
    )


def test_subtract_decimals_split_decimals():
    assert (("1", "2"), ("3", "4")) == _subtract_decimals_split_decimals(first="1.2", second="3.4")


def test_subtract_decimals_put_zeros_on_end():
    assert ("120", "345") == _subtract_decimals_put_zeros_on_end(first_dec="12", second_dec="345")
    assert ("120000", "345678") == _subtract_decimals_put_zeros_on_end(first_dec="12", second_dec="345678")
    assert ("125", "340") == _subtract_decimals_put_zeros_on_end(first_dec="125", second_dec="34")
    assert ("125678", "340000") == _subtract_decimals_put_zeros_on_end(first_dec="125678", second_dec="34")


def test_subtract_decimals_split_decimals2():
    assert (("1", "2"), ("3", "4")) == _subtract_decimals_split_decimals2(first="1.2", second="3.4")


def test_subtract_decimals_actually_subtract_them():
    assert ("-2", "2") == _subtract_decimals_actually_subtract_them(
        first_whole="1", first_dec="2", second_whole="3", second_dec="4"
    )
    assert ("2", "2") == _subtract_decimals_actually_subtract_them(
        first_whole="3",
        first_dec="4",
        second_whole="1",
        second_dec="2",
    )
