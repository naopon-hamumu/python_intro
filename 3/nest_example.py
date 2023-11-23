for a in range(1, 4):
    print('a=', a)
    for b in range(1, 4):
        print('     b=', b)

for a in range(1, 10):
    print()
    for b in range(1, 10):
        print(f'{a}x{b}={a*b} ', end='') # end=''は改行をなくす
