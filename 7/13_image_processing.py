import cv2

img = cv2.imread('7/data/block.jpeg')
height = img.shape[0] # 画像の高さを取得
width = img.shape[1] # 画像の幅を取得
resized_img = cv2.resize(img, (int(width/2), height))
cv2.imwrite('7/data/resized.jpg', resized_img)

gray_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
cv2.imwrite('7/data/gray.jpg', gray_img)

canny_img = cv2.Canny(img, 50, 100)
cv2.imwrite('7/data/canny.jpg', canny_img)
