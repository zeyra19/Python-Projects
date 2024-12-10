# özet: Class bazlı ve testin durumunu bildiren pytest yaz


class TestDictionaryData:

    def setup_method(self, method):
        print(f"Başlayan işlem şu: {method.__name__}")
        self.data = {"key": "value"}
        self.data2 = {"value": "key"}

    def test_check_key(self):
        assert "key" in self.data

    def test_check_value(self):
        assert "value" in self.data2

    def test_check_key_value(self):
        assert self.data["key"] == "value"

    def test_check_value_key(self):
        assert self.data2["value"] == "key"