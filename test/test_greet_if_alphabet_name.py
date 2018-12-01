import pytest
from src import script


@pytest.mark.parametrize(("name", "expected"), [
    ("Jason", "Hello, Jason!"),
    ("Django", "Hello, Django!"),
])
def test_response(name, expected):
    assert script.greet_if_alphabet_name(name) == expected


@pytest.mark.parametrize("name", [
    "ouh;ouaea", "vaoue;aoaあああ", "たかし"
])
def test_error(name):
    with pytest.raises(ValueError) as e:
        script.greet_if_alphabet_name(name)

    # エラーメッセージを調べるには、エラーオブジェクトを調べるしかないようです。
    # この場合、e.valueがValueErrorのインスタンス
    assert str(e.value).startswith("Sorry! This method is English Only!")