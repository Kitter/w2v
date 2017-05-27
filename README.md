# abst
cozysfc/twstreamで集めたデータを対象に以下のコマンドラインツールを実装
* 前処理
  * 正規表現で記号など__symbol__といった文字で置換
  * 半角カナを全角カナに変換
  * 動詞活用形を原型に変換
  * 分かち書きにする
* word2vec用コーパス作成
* word2vecの学習

# setup
mecab, mecab-ipadic, mecab-ipadic-neologdのinstall
```
mkdir src
cd src
brew install mecab mecab-ipadic curl xz git
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
```

user dictionaryの追加
```
cd dict
sh compile.sh
```

標準以外の辞書を使う場合
システム辞書とユーザ辞書のパスをexport
```
export USRDIC="/path/to/mydict.dic"
export SYSDIC="/path/to/mecab-ipadic-neologd/"
```

ライブラリのインストール
```
pip install -r requirements.txt
```
