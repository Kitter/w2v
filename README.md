# abst
改行区切りのテキストデータを対象に以下のコマンドラインツールを実装
* 前処理
  * 半角カナを全角カナに変換
  * 動詞活用形を原型に変換
  * 分かち書きにする
* word2vec用コーパス作成
* word2vecの学習

# setup
## mecab, mecab-ipadic, mecab-ipadic-neologdのinstall
```
mkdir src
cd src
brew install mecab mecab-ipadic curl xz git
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
```

## 必要ならばmydict.dicの追加
```
cd dict
sh compile.sh
```

## 標準以外の辞書を使う場合
システム辞書かユーザ辞書(もしくは両方)のパスをexport
```
export USRDIC="/path/to/mydict.dic"
export SYSDIC="/path/to/mecab-ipadic-neologd/"
```

## ライブラリのインストール
```
pip install -r requirements.txt
```

# 使い方

## help
```
python w2v --help
```

## build corpus
```
python w2v build corpus hoge.txt corpus.txt
```

## build word2vec model
```
python w2v build word2vec corpus.txt model.w2v
```

## word2vecを読み込んだ状態でipythonを開く
```
python w2v shell model.w2v
```
