import pytest

@pytest.mark.parametrize("name",["张三","李四","王五"])
def test_name(name):
    print(name)