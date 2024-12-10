# özet: pytest de @pytest.fixtures kullandığın bir örnek yap
import pytest
from example_28 import hi, bye, i_love_you


@pytest.fixture()
def ogulcan():
    return "Oğulcan"


def test_hi(ogulcan):
    assert hi(ogulcan) == "Selam Oğulcan"


def test_bye(ogulcan):
    assert bye(ogulcan) == "Görüşürüz Oğulcan"


def test_i_love_you(ogulcan):
    assert i_love_you(ogulcan) == "Seni Seviyorum Oğulcan"