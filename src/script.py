import re
from pathlib import Path


def greet(name):
    """挨拶を返す。

    Args:
        name [str]: 名前
    Returns:
        str: 英語の挨拶

    """
    return f"Hello, {name}!"


def greet_if_alphabet_name(name):
    """英語の名前のときに挨拶を返す。

    Args:
        name [str]: 名前
    Returns:
        str: 英語の挨拶
    Raises:
        ValueError: アルファベット名前でなかった場合

    """
    if re.search(r"[^a-zA-Z]", name):
        raise ValueError("Sorry! This method is English Only!")
    return f"Hello, {name}!"


def greet_and_remember(name):
    """ログを参照して挨拶を返す。

    Args:
        name [str]: 名前
    Returns:
        str: 日本語の挨拶

    """
    log = LogFile("./logs/names.txt")
    if log.includes(name):
        return f"また会いましたね、{name}さん"
    else:
        log.append(name)
        return f"はじめまして、{name}さん"


class LogFile(object):
    def __init__(self, filename):
        self.path = Path(filename)
    
    def includes(self, name):
        self.touch()
        with self.path.open(mode="r") as f:
            known_names = {n.rstrip("\n") for n in f} 
        return name in known_names
    
    def append(self, name):
        self.touch()
        with self.path.open(mode="a") as f:
            f.write(name)
            f.write("\n")
        
    def touch(self):
        self.path.parent.mkdir(exist_ok=True)
        self.path.touch(exist_ok=True)