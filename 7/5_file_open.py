f = open('7/data/visitor_record.txt', 'r', encoding='UTF-8') # ファイルを開き、ファイルオブジェクトを取得
lines = f.readlines() # ファイルの中身を読み込む

for line in lines: # 1行ずつ変数lineに取り出して処理
    if '東京都' in line:
        print(line.replace('\n', ''))

f.close() # ファイルを閉じる
