#özet: fonksiyon bazlı pytest örnekleri
import pytest
import example_26 as example_26


def test_add():
    result = example_26.add(number_1=1, number_2=4)
    assert result == 5


def test_add_string():
    result = example_26.add(number_1="Oğulcan ", number_2="<3 Zeyra ")
    assert result == "Oğulcan <3 Zeyra "


def test_divide():
    result = example_26.divide(number_1=20, number_2=5)
    assert result == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        example_26.divide(number_1=2, number_2=0)
