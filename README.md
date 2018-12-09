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

  "xticks": null,
  "yticks": null,

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

### ticks
xticksは縦軸、yticksは横軸の刻み幅を決めるパラメータである。  
以下に設定例を示す。
```
{
  // x座標を、0.0から1.0まで0.1の刻み幅で表示
  "xticks": {
    "begin": 0.0,
    "end"  : 1.1,
    "step" : 0.1
  }
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
