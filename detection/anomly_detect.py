import cv2
import numpy as np


def find_rect_of_target_color(image):
    print("検知方法「find rectangle of target color」を利用")
    result=None
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    mask = np.zeros(h.shape, dtype=np.uint8)
    mask[((h > 0) | (h < 43)) & (s > 128)] = 255
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects.append(np.array(rect))
    cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (0, 0, 255), thickness=2)
    cv2.putText(image, 'error', (np.array(rect)[0], np.array(rect)[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                (0, 0, 255), 2)
    #"""
    print("「find rectangle of target color」の結果と画像を戻す")
    return result,image

def find_by_labeling(image):
    print("検知方法「find_by_labeling」を利用")
    result = None
    """
    https://dronebiz.net/tech/opencv/labeling
    """

    """
    gray_src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print(gray_src)
    # 前処理（平準化フィルターを適用した場合）
    # 前処理が不要な場合は下記行をコメントアウト
    blur_src = cv2.GaussianBlur(gray_src, (5, 5), 2)

    # 二値変換
    # 前処理を使用しなかった場合は、blur_srcではなくgray_srcに書き換えるする
    mono_src = cv2.threshold(blur_src,127, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow("mono_1", mono_src)

    # ラベリング結果書き出し用に二値画像をカラー変換
    color_src01 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
    color_src02 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)

    # ラベリング処理
    label = cv2.connectedComponentsWithStats(mono_src)

    # オブジェクト情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)

    # オブジェクト情報を利用してラベリング結果を画面に表示
    for i in range(n):
        # 各オブジェクトの外接矩形を赤枠で表示
        x0 = data[i][0]
        y0 = data[i][1]
        x1 = data[i][0] + data[i][2]
        y1 = data[i][1] + data[i][3]
        cv2.rectangle(color_src01, (x0, y0), (x1, y1), (0, 0, 255))
        cv2.rectangle(color_src02, (x0, y0), (x1, y1), (0, 0, 255))

        # 各オブジェクトのラベル番号と面積に黄文字で表示
        cv2.putText(color_src01, "ID: " + str(i + 1), (x1 - 20, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        cv2.putText(color_src01, "S: " + str(data[i][4]), (x1 - 20, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

        # 各オブジェクトの重心座標をに黄文字で表示
        cv2.putText(color_src02, "X: " + str(int(center[i][0])), (x1 - 30, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1,
                    (0, 255, 255))
        cv2.putText(color_src02, "Y: " + str(int(center[i][1])), (x1 - 30, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                    (0, 255, 255))

    
    # 結果の表示
    cv2.imshow("color_src01", color_src01)
    #cv2.imshow("color_src02", color_src02)
    """
    print("「find_by_labeling」の結果と画像を戻す")
    return result, image
