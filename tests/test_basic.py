import pytest
import template

class TestClass:
    def test_sum_3_4(self):
        assert template.sum(3, 4) == 7

    def test_template_asserts_true(self):
        assert template.main()

if __name__ == "__main__":
    pytest.main()
