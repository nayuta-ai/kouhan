import cv2
import glob
import os
import matplotlib.pyplot as plt
import numpy as np

SIZE = 416
path ="imgs/*.jpg"
save_path = "VOCdevkit/VOC2007/JPEGImages/img"


#画像の読み込み
path_arr = glob.glob(path)


# アスペクト比固定で指定サイズ内に収まるようにリサイズする
def scale_box(img, width, height):
    scale = min(width / img.shape[1], height / img.shape[0])
    return cv2.resize(img, dsize=None, fx=scale, fy=scale)

# 余白部分を黒で埋める
def add_margin(img,SIZE):
    pad_list = np.array([0 for i in range(SIZE)])
    height = img.shape[0]
    width = img.shape[1]
    diff_height = SIZE - height
    diff_width = SIZE - width

    # 縦を変更
    if diff_height <0:
        pass
    elif diff_height == 0:
        pass
    elif diff_height >0:
        while img.shape[0] <416:
            img = np.insert(img, img.shape[0], 0, axis=0)

    # 横を変更
    if diff_width <0:
        pass
    elif diff_width == 0:
        pass
    elif diff_width >0:
        while img.shape[1] <416:
            img = np.insert(img, img.shape[1], 0, axis=1)
    return img

# 実行
for i in range(len(path_arr)):
    img = cv2.imread(path_arr[i])
    dst = scale_box(img,SIZE,SIZE)
    dst = add_margin(dst,SIZE)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
    plt.imsave(save_path+str(i)+".jpg",dst)
    print(f"{img.shape} -> {dst.shape}")