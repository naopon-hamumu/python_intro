total = 0
for i in range(10): # 0から9の値を順番に変数iに代入
    total += i
    if total > 20:
        break
print(i, total)
