### モジュール

- モジュールのインポート
  ```
  import モジュール名
  ```

- モジュールに別名をつけてインポートする
  ```
  import モジュール名 as 別名
  ```

- 関数単位でのインポート
  ```
  from モジュール名 import 関数名
  ```

- mathモジュール<br>
  | 関数 | 説明 |
  | :---: | :---: |
  | ceil(x) | xの値以上の最小の整数を返す |
  | cos(x) | xのコサインを返す。xの単位はラジアン |
  | floor(x) | xの値以下の最大の整数を返す |
  | exp(x) | e（ネイピア数）のx乗を返す |
  | log(x) | xの自然対数を返す |
  | sqrt(x) | xの平方根を返す |
  | sin(x) | xのサインを返す。xの単位はラジアン |
  | tan(x) | xのタンジェントを返す。xの単位はラジアン |
  | radians(x) | 角度xをラジアンに変換した値を返す |
  | atan(x) | xのアークタンジェントを返す |

  ```
  math.関数名(引数)
  ```

  | 定数名 | 値 |
  | :---: | :---: |
  | pi | 円周率 |
  | e | 自然対数の底 |

- randomモジュール（乱数）
  ```
  import random
  random.radint(1, 6)
  2
  ```
  ```
  import random
  janken = ['グー', 'チョキ', 'パー']
  random.choice(janken)
  'グー'
  ```

  | 関数 | 説明 |
  | :---: | :---: |
  | random() | 0以上1未満のランダムな浮動小数点数を返す |
  | radint(a, b) | a以上b以下のランダムな整数を返す |
  | randrange(x) | 0から(x-1)までのランダムな整数を返す |
  | choice(list) | listからランダムに1つ選んだ要素を返す |

- turtle：グラフィックス描画

- matplotlib：Pythonでグラフを描画する
  - [ドキュメント](https://matplotlib.org/contents.html)

  - 使用例
    ```
    import matplotlib
    import matplotlib.pyplot as plt

    pref_count_dict = {}
    with open('7/data/visitor_record.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            data, pref, num_adult, num_children = line.split(
                num_all = int(num_adult) + int(num_children))
            if pref in pref_count_dict:
                pref_count_dict[pref] += num_all
            else:
                pref_count_dict[pref] = num_all

    # 訪問者数でソート
    pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x:x[1], reverse=True)

    labels = [] # グラフのラベル（都道府県名）
    values = [] # グラフの値（訪問者数）
    for 1 ,v in pref_count_sorted:
        # 取り出したラベルと値をリストに格納
        labels.append(1)
        values.append(v)

    # グラフをファイルに出力するために必要な記述
    matplotlib.use('Agg')
    # フォントの設定
    plt.rcParams['font.family'] = 'Yu Gothic'
    # ラベルを縦書きにする
    plt.xticks(rotation=270)
    # グラフを作成
    plt.bar(range(0, len(pref_count_sorted)), values, tick_label=labels)
    # グラフを画像として保存
    plt.savefig('graph.png')
    ```

- OpenCV：
  - [ドキュメント](https://docs.opencv.org/)

  - 使用例
    ```
    import cv2

    img = cv2.imread(7/data/block.jpg) # 画像ファイルを読み込む
    cv2.imshow('img', img) # 画像を表示
    cv2.waitKey(0) # 画像を表示したウィンドウで、何かキーが押されるのを待つ
    cv2.destroyAllWindows() # ウィンドウを閉じる
    ```

  - メソッド
    * サイズを変国した画像オブジェクトを返す
      ```
      cv2.resize(元画像, (幅, 高さ))
      ```

    * グレースケール画像にする
      ```
      cv2.resize(元画像, cv2.COLOR_RGBA2GRAY)
      ```

    * エッジ検出
      ```
      cv2.Canny(元画像, パラメータ1, パラメータ2)
      ```

    * 画像の保存
      ```
      cv2.imwrite(ファイルパス, 画像オブジェクト)
      ```

    * 円の検索
      ```
      HoughCircles(対象とする画像, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
      ```

    * 円の描画
      ```
      cv2.circle(画像オブジェクト, (中心のx座標, 中心のy座標), 半径, 色情報, 線の太さ )
      ```
