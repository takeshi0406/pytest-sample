import click
from importlib import import_module
from src import script


@click.command()
@click.option("--name", "-n", required=True, type=str)
@click.option("--arg", "-a", required=True, type=str)
def cmd(name, arg):
    """コマンドを実行する。

    Args:
        name [str]: 実行関数名
        arg [str]: 実行引数

    """
    try:
        func = getattr(script, name)
        print(func(arg))
    except ImportError:
        raise RuntimeError("対応するコマンドが見つかりません！")


def main():
    cmd()


if __name__ == '__main__':
    main()
