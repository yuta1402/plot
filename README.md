# Plot
## 設定ファイル
設定ファイルは、main.pyと同一ディレクトリに`settings.json`として置いておく。  
下記は`settings.json`のテンプレートである。
```
{
  "datafiles": [
  ],

  "xlabel": "",
  "ylabel": "",
  "xscale": "linear",
  "yscale": "linear",

  "xmin": null,
  "xmax": null,
  "ymin": null,
  "ymax": null,

  "grid": {
    "which": "major",
    "color": "black",
    "linestyle": "--"
  },

  "savefig_name": ""
}
```

### datafiles
入力のデータファイルは下記のように設定する。
```
{
    "datafiles": [
        ["data0.txt", "label0"],
        ["data1.txt", "label1"],
        ...
        ["datan.txt", "labeln"]
    ],
}
```

### savefig_name
グラフをファイルに出力する場合は、ファイル名を指定する。
```
{
    "savefig_name": "test.pdf"
}
```
空文字の場合は、`plt.show()`が実行される。
