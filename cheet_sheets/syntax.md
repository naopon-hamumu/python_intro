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
