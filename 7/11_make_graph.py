import matplotlib
import matplotlib.pyplot as plt

pref_count_dict = {}
with open('7/data/visitor_record.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data, pref, num_adult, num_children = line.split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

# 訪問者数でソート
pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x:x[1], reverse=True)

labels = [] # グラフのラベル（都道府県名）
values = [] # グラフの値（訪問者数）
for l, v in pref_count_sorted:
    # 取り出したラベルと値をリストに格納
    labels.append(1)
    values.append(v)

# グラフをファイルに出力するために必要な記述
matplotlib.use('Agg')
# フォントの設定
plt.rcParams['font.family'] = 'sans-serif'
# ラベルを縦書きにする
plt.xticks(rotation=270)
# グラフを作成
plt.bar(range(0, len(pref_count_sorted)), values, tick_label=labels)
# グラフを画像として保存
plt.savefig('7/data/graph.png')
