import cv2 as cv
import numpy as np

def picchange():
    line_num = 0
    img1 = cv.imread('shot.jpg', 0)
    # 长宽
    height1, width1 = img1.shape
    # cv.imshow('img1', img0)
    # 腐蚀 因为黑白相反
    kernel1 = np.ones((3, 3), np.uint8)
    img1 = cv.erode(img1, kernel1)
    # 二值化
    ret, img1 = cv.threshold(img1, 240, 255, cv.THRESH_BINARY)
    img1 = cv.bitwise_not(img1)
    if (height1 < 200) | (width1 < 200):
        img0 = np.zeros((600, 800), np.uint8)
        img0[1:height1+1, 1:width1+1] = img1
        img1 = img0
    # cv.imshow('img1', img1)

    '''
    contours, hierarchy = cv.findContours(img1.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 统计选择的检测区域中的轮廓（有效轮廓）
    valid_cntrs = []  # 空列表 valid_cntrs 用于存放有效轮廓

    for cntr in contours:  # 遍历找到的所有轮廓
        x, y, w, h = cv.boundingRect(cntr)  # 轮廓的坐标
        if (cv.contourArea(cntr) >= 25) & (h < height1) & (h < width1):
            dmy = cv.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
            line_num += 1
            cv.imshow('img', dmy)
    '''

    for i in range(2):
        for j in range(width1):
            img1[i][j] = 0
    for i in range(height1-2, height1):
        for j in range(width1):
            img1[i][j] = 0

    for i in range(height1):
        for j in range(2):
            img1[i][j] = 0
    for i in range(height1):
        for j in range(width1-2, width1):
            img1[i][j] = 0

    low_threshold = 10
    high_threshold = 20
    edges = cv.Canny(img1, low_threshold, high_threshold)
    # cv.imshow('edges', edges)
    rho = 5
    theta = np.pi/180
    threshold = 50
    min_line_length = 30
    max_line_gap = 15
    line_image = np.copy(img1)
    lines = cv.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    for line in lines:
        for x1, y1, x2, y2 in line:
            line_image = cv.line(line_image, (x1, y1), (x2, y2), 255, 1)


    # cv.imshow('img2', line_image)

    for i in range(2):
        for j in range(width1):
            line_image[i][j] = 0
    for i in range(height1-2, height1):
        for j in range(width1):
            line_image[i][j] = 0

    for i in range(height1):
        for j in range(2):
            line_image[i][j] = 0
    for i in range(height1):
        for j in range(width1-2, width1):
            line_image[i][j] = 0

    contours, hierarchy = cv.findContours(line_image.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 统计选择的检测区域中的轮廓（有效轮廓）
    valid_cntrs = []  # 空列表 valid_cntrs 用于存放有效轮廓

    for cntr in contours:  # 遍历找到的所有轮廓
        x, y, w, h = cv.boundingRect(cntr)  # 轮廓的坐标
        if (cv.contourArea(cntr) >= 25) & (h < height1) & (h < width1):
            line_image = cv.rectangle(line_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            line_num += 1

    # cv.imshow('img3', line_image)

    if line_num > 35:
        line_num = 0
    # print(line_num)
    return line_num


