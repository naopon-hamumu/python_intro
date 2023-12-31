### 構文

- if文
  ```
  if 条件式:
      処理内容
  elif 条件式:
      処理内容
  else:
      処理内容
  ```

  * 内包表記
    ```
    [式 for 変数 in 反復可能なオブジェクト if 条件式]

    data0 = ['apple', 'orange', 'banana', 'avocado']
    data1 = [s for s in data0 if s[0] == 'a']
    print(data1) # => ['apple', 'avocado']
    ```

- 繰り返し
  - while文
    ```
    while 条件式:
        処理内容
    ```

  - for文（Rubyではeach文）
    ```
    for 変数 in 反復可能オブジェクト:
        処理内容
    ```

    * 内包表記
      ```
      [式 for 変数 in 反復可能なオブジェクト]

      data = [2**n for n in range(1, 11)]
      data = [str(n)+'月' for n in range(1, 13)]
      ```

  - 強制的にブロックから抜け出す
    ```
    break
    ```

  - ループ内の処理をスキップする
    ```
    continue
    ```

  - 値を呼び出し元に戻す
    ```
    return
    ```

  - 何もしない
    ```
    pass
    ```

- ラムダ式（lambda式）
  ```
  lambda 引数列: 戻り値
  ```

- try~except文（例外処理）
  ```
  try:
      本来実行したい処理
  except:
      例外が発生した時の処理
  else:
      例外が発生しなかった時の処理
  finally:
      例外の有無に関わらず実行される処理
  ```
