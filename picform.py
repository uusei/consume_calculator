import cv2 as cv


def picchange():
    line_num = 0
    img1 = cv.imread('shot.jpg', 0)

    height1, width1 = img1.shape

    for i in range(4):
        for j in range(width1):
            img1[i][j] = 255
    for i in range(height1-4, height1):
        for j in range(width1):
            img1[i][j] = 255

    for i in range(height1):
        for j in range(4):
            img1[i][j] = 255
    for i in range(height1):
        for j in range(width1-4, width1):
            img1[i][j] = 255

    ret, img = cv.threshold(img1, 125, 255, cv.THRESH_BINARY)
    # cv.imshow('img1', img)

    contours, hierarchy = cv.findContours(img.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 统计选择的检测区域中的轮廓（有效轮廓）
    valid_cntrs = []  # 空列表 valid_cntrs 用于存放有效轮廓

    for cntr in contours:  # 遍历找到的所有轮廓
        x, y, w, h = cv.boundingRect(cntr)  # 轮廓的坐标
        if (cv.contourArea(cntr) >= 50) & (h < height1) & (h < width1):
            dmy = cv.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
            line_num += 1

    if line_num > 30:
        line_num = 0
    # print(line_num)
    return line_num

