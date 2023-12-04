import cv2

img = cv2.imread('7/data/block.jpeg') # 画像ファイルを読み込む
cv2.imshow('img', img) # 画像を表示
cv2.waitKey(0) # 画像を表示したウィンドウで、何かキーが押されるのを待つ
cv2.destroyAllWindows() # ウィンドウを閉じる
