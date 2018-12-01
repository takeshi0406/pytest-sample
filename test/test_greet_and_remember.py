import pytest
from src import script


@pytest.mark.parametrize(("exists", "expected"), [
    (True, "また会いましたね、Jasonさん"),
    (False, "はじめまして、Jasonさん")
])
def test_return_value(mocker, exists, expected):
    # クラスのモックをセットする
    # 冗長な気がするので、もっと良い書き方があるのかもしれません
    insmock = mocker.Mock()
    insmock.includes.return_value = exists
    mocker.patch.object(script, "LogFile", mocker.Mock(return_value=insmock))

    # 期待値のチェック
    assert script.greet_and_remember("Jason") == expected


def test_if_exists(mocker):
    insmock = mocker.Mock()
    insmock.includes.return_value = True
    mocker.patch.object(script, "LogFile", mocker.Mock(return_value=insmock))

    assert script.greet_and_remember("Jason") == "また会いましたね、Jasonさん"
    insmock.append.assert_not_called()


def test_if_not_exists(mocker):
    insmock = mocker.Mock()
    insmock.includes.return_value = False
    mocker.patch.object(script, "LogFile", mocker.Mock(return_value=insmock))

    assert script.greet_and_remember("Jason") == "はじめまして、Jasonさん"
    insmock.append.assert_called_once()