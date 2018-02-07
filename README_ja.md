# Mirage Linemode

カスタマイズできる [ranger](https://ranger.github.io/) 用の Linemode プラグイン.

![mirage_linemode](https://raw.githubusercontent.com/hankei6km/mirage_linemode/master/images/mirage_linemode.png)

* emoji 等を使ってフォルダー:file_folder:やファイル:page_facing_up:のアイコンを表示.
* XDG のユーザーディレクトリ(ローカライズされた名前にも対応するはずです)や特定のディレクトリ/ファイル(例えば `setup.py` や `package.json` `tests` など)へのアイコン指定.

等をカスタマイズできます.

mirage\_linemode は  [ranger\_devicons](https://github.com/alexanderjeurissen/ranger_devicons.git) をすごく参考にしています.


## Installation

パッケージのインストールと初期化.

```
# pip install mirage_linemode
$ mirage_linemode_ctrl init
```


## Usage

プラグインの有効化.

```
$ mirage_linemode_ctrl enable
```


## Uninstallation

```
$ mirage_linemode_ctrl disable
# pip uninstall mirage_linemode
```

カスタマイズしたテーマファイル等を削除したい場合は、
`<xdg config home>/mirage-linemode` を削除.
(`<xdg config home>` は多くの場合 `$HOME/.config` です)


## Theme

mirage\_linemode は活動状態になる毎に、
`<xdg config home>/mirage-linemode/mirage_linemode_theme.yml` をテーマとして取り込みます.
テーマを変更する場合は、このファイルを編集します.

emoji に対応した VTE を利用しているターミナルエミュレーター等(例えばTermite)では、emoji を組み込んだテーマも使えます.
ただし、文字幅の扱いが混沌としているので行の幅がガクガクになることが多いです.
いちおう、若干ながら軽減させる設定も用意はしてありますが、面倒なわりに効果はそれほどでもありません.
その辺はおおらかな心で我慢してください.


## emojiの文字幅対応

以下の手順でアイコンとしての表示幅をある程度は修正できます.

1. `$ mirage_linemode_ctrl theme -w` を実行すると以下のようなリストが表示されるので、先頭の数字(ranger 側で認識している文字幅)が `2` でありながら、右側の縦線が他よりも引っ込んでいる文字をメモする.
<p><img src="https://raw.githubusercontent.com/hankei6km/mirage_linemode/master/images/theme_chars_width_list.png"></p>

2. `<xdg config home>/mirage-linemode/mirage_linemode_config.yaml` をエディタで開き、メモしておいた文字を
`fix_chars_width.for_term.defaul` に配列として記述.
3. `fix_chars_width.enabled` を `true` とする.
<p><img src="https://raw.githubusercontent.com/hankei6km/mirage_linemode/master/images/config_fix_chars_width.png"></p>

ただし、行右側のファイルサイズ等の表示はガクガクのままです.
上記設定に加えて、`fix_chars_width.force_right_align` も `true` にすると軽減できますが、親ディレクトリ等の表示にもファイルサイズ等が表示されるようになります.


## License

Copyright (c) 2018 hankei6km

Licensed under the MIT License. See LICENSE.txt in the project root.
