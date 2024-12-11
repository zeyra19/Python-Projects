# özet: pytest de mark and paramitirize: test sürecini daha düzenli ve esnek hale getirmek için kullanılır

import pytest
import time


@pytest.mark.slow
def test_slow_function():
    time.sleep(3)
    assert True
    print("Test 3 saniye sonra tamamlandı")


@pytest.mark.fast
def test_fast_function():
    assert True
    print("Test çok hızlı tamamlandı")


@pytest.mark.xfail(reason="Bu fonksiyon hata vericek")
def test_known_issues():
    assert False


@pytest.mark.skip(reason="Henüz tamamlanmadı")
def test_incomplete():
    assert False


# özet: fonksiyon oluştur onun üzerine mark and paramitirize uygula
def multiply(a, b):
    return a * b


@pytest.mark.parametrize("a, b, expected", [(2, 4, 8), (10, 3, 30)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
