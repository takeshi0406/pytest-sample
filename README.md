# pytest-sample

pipenvを利用してインストールしてください。

```bash
pipenv shell
pipenv install --dev
```

これでテストコードが実行できます。

```bash
pytest test
```

ついでに、実行ファイルを指定して実際に動かすこともできます。

```python
python main.py  -n greet -a "Jason"
Hello, Jason!
```