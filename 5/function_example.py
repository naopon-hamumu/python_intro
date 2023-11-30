def say_hello():
    print('こんにちは')
    print('今日はいい天気ですね')

say_hello()
say_hello()

def function_a():
    print('function_aの処理です')

def function_b():
    print('function_bの処理開始')
    function_a
    print('function_bの処理終了')

print('function_bを呼び出します')
function_b
