

########################################
 # 注：除程序中注明不能使用第三方库外，其他操作可使用第三方库
 # © Yihang.ai
 # Version: 1.4
#########################################


'''
 * Project1: 计算两三角形是否有交集
 * 要求： 
 *  1） 计算给定两个三角形是否有交集
 *  2） 输出以布尔结果返回
 *  3） 计算过程不可直接使用numpy等第三方库
 * 输入： 三角形描述，以list格式输入，每个三角形有6个数据表示 [x1, y1, x2, y2, x3, y3]
 *       分别表示三角形三个顶点的坐标
 * 输出： 计算所有三角形是否有交集，有交集返回True，无交集返回False
'''
def has_overlap(triangle1, triangle2):
    if len(triangle1) != 6 or len(triangle2) != 6:
        return False

    # 依次判断三角形1的每个边是否和三角形2的每个边相交, 有的话就证明有交集
    for i in (0, 2, 4):
        x1_t1, y1_t1 = (triangle1[i], triangle1[i + 1])
        x2_t1, y2_t1 = (triangle1[(i + 2) % 6], triangle1[(i + 3) % 6])
        for j in (0, 2, 4):
            x1_t2, y1_t2 = (triangle1[j], triangle1[j + 1])
            x2_t2, y2_t2 = (triangle1[(j+2)%6], triangle1[(j+3)%6])
            if intersect_two_lines(x1_t1, y1_t1, x2_t1, y2_t1, x1_t2, y1_t2, x2_t2, y2_t2):
                return True
    '''
    # 依次判断三角形1的每个边是否和三角形2的每个边相交, 有的话就证明有交集（另一种方式）
    for i in (0, 2, 4):
        # k_t1, b_t1为第一个三角形的一条边的斜率和截距
        x1_t1, y1_t1 = (triangle1[i], triangle1[i+1])
        x2_t1, y2_t1 = (triangle1[(i+2)%6], triangle1[(i+3)%6])
        k_t1 = (y2_t1 - y1_t1) / (x2_t1 - x1_t1)
        b_t1 = y1_t1 - k_t1 * x1_t1
        for j in (0, 2, 4):
            # k_t2, b_t2为第一个三角形的一条边的斜率和截距
            x1_t2, y1_t2 = (triangle1[i], triangle1[i + 1])
            x2_t2, y2_t2 = (triangle1[(i+2)%6], triangle1[(i+3)%6])
            k_t2 = (y2_t2 - y1_t2) / (x2_t2 - x1_t2)
            b_t2 = y1_t2 - k_t2 * x1_t2

            # 若两直线平行，则不会有交点
            if k_t1 == k_t2:
                continue

            # x, y 为两条直线交点坐标：
            x = - ((b_t1 - b_t2)/(k_t1 - k_t2))
            y = k_t1 * x + b_t1

            # 判断(x,y)是否在同时在两个线段内，有相交的边则有重叠，返回True
            if min(x1_t1, x2_t1) <= x <= max(x1_t1, x2_t1) and min(y1_t1, y2_t1) <= y <= max(y1_t1, y2_t1):
                if min(x1_t2, x2_t2) <= x <= max(x1_t2, x2_t2) and min(y1_t2, y2_t2) <= y <= max(y1_t2, y2_t2):
                    return True'''

    # 判断两个三角形是否为包含关系
    # 如果一个三角形包含了另一个三角形的一个顶点，则该三角形一定包含另一个三角形（因为代码运行到这里已经能够确定两三角形无任何线段相交）
    # 判断三角形t1的第一个顶点是否在三角形t2中：
    (x1_t1, y1_t1) = triangle1[0], triangle1[1] # 三角形t1的第一个顶点
    # 只要三角形t1的第一个顶点一直在每一个三角形t2边的向量的左侧，则该顶点在三角形t2中
    # 因此，遍历三角形t2的三个边向量(AB)并计算该边向量和到三角形t1的第一个顶点的向量(AX)的向量积
    t1_in_t2 = True
    for i in (0, 2, 4):
        x1_t2, y1_t2 = (triangle2[i], triangle2[i+1])
        x2_t2, y2_t2 = (triangle2[(i+2)%6], triangle2[(i+3)%6])

        # 得到两向量
        vector_AB = (x2_t2 - x1_t2, y2_t2 - y1_t2)
        vector_AX = (x1_t1 - x1_t2, y1_t1 - y1_t2)

        # 计算向量积: AB*AX
        cross_product = vector_AB[0] * vector_AX[1]  - vector_AB[1] * vector_AX[0]

        # 若小于等于0，则三角形t1的第一个顶点在右侧或者共线，t2不包含t1
        if cross_product <= 0:
            t1_in_t2 = False
            break
    if t1_in_t2:
        return t1_in_t2

    t2_in_t1 = True
    # 逻辑类似与上述，这次检查t2是否在t1内
    (x1_t2, y1_t2) = triangle2[0], triangle2[1]  # 三角形t1的第一个顶点
    for i in (0, 2, 4):
        x1_t1, y1_t1 = (triangle1[i], triangle1[i+1])
        x2_t1, y2_t1 = (triangle1[(i+2)%6], triangle1[(i+3)%6])

        # 得到两向量
        vector_AB = (x2_t1 - x1_t1, y2_t1 - y1_t1)
        vector_AX = (x1_t2 - x1_t1, y1_t2 - y1_t1)

        # 计算向量积
        cross_product = vector_AB[0] * vector_AX[1]  - vector_AB[1] * vector_AX[0]

        # 若小于等于0，则三角形t1的第一个顶点在右侧或者共线，t2不包含t1
        if cross_product <= 0:
            t2_in_t1 = False
            break
    if t2_in_t1:
        return t2_in_t1


    return False

# 该方法判断两条线段是否相交
def intersect_two_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    :param x1, y1, x2, y2为第一条线段的坐标
    :param x3, y3, x4, y4为第二条线段的坐标
    :return: 两直线是否相交
    '''
    # 先判断线段构成的矩形受否相交，若矩形未相交则快速返回False
    if (max(x1, x2) > min(x3, x4) and max(y1, y2) > min(y3, y4)) or (max(x3, x4) > min(x1, x2) and max(y3, y4) > min(y1, y2)):
        # 进行跨立实验
        if cross(x1, y1, x2, y2, x3, y3) * cross(x1, y1, x2, y2, x4, y4) <= 0 and cross(x3, y3, x4, y4, x1, y1) * cross(x3, y3, x4, y4, x2, y2) <= 0:
            return True
    else:
        return False

# 输入三个点坐标进行叉积运算
# 返回v1:p1p2和v2:p1p3的交叉积
def cross(x1, y1, x2, y2, x3, y3):
    x_v1 = x2 - x1
    y_v1 = y2 - y1
    x_v2 = x3 - x1
    y_v2 = y3 - y1
    return (x_v1 * y_v2) - (x_v2 * y_v1)


'''
 * Project2: 给定输入数据流，每来一个数据，求取最新N个数据中中间大小M（M≤N）个数据的均值和方差
 * 要求： 
 *  1） 给定数据流，求取最新N个数据中满足条件的均值和方差
 *  2） 条件为：N个数据按大小排序后，取中间M（M≤N）个数据
 *  3） 设定 N=10， M=6
 *  4） 计算过程不可使用任何第三方库
 * 注意：最新的N个数据表示按照数据流顺序最新的数据，比如 数据流为 [2,3,5,1,5,6]，则最新3个数据为[1,5,6]
 * 输入： 数据流，以list形式输入，根据其下标表示数据流的输入顺序，如 [3, 5, 6, 10, 2 ...]，
         表示输入数据流为 3, 5, 6, 10, 2 ...
 * 输出： 均值和方差，返回两个list，分别为均值 avg 和方差 var
 *       开始时，数据量<M时，返回已知数据的均值和方差
'''
def get_avg_var(data,   N, M):
    length  = len(data)
    avg     = range(length)
    var     = range(length)
    #
    # code here
    #
    return avg,var


'''
 * Project3: 单应性变换
 * 要求： 
 *  1） 已知一个平面上的4个点（A、B、C、D），经过两个针孔相机分别成像得到4个点的图像坐标分别为
 *          相机1： (xA1, yA1)，(xB1, yB1), (xC1, yC1), (xD1, yD1)
 *          相机2： (xA2, yA2)，(xB2, yB2), (xC2, yC2), (xD2, yD2),
 *      计算相机1的图像到相机2图像的单应矩阵，并转换相机2图像中的点坐标到相机1图像坐标中
 *  2） 计算单应矩阵及求取点坐标时不可直接使用第三方库
 *  3） 除2）要求的过程外，其他过程如求矩阵的逆、迹、秩可根据个人习惯使用第三方库
 *  4） 点的坐标以二维列表形式给出，如 [[1, 2], [3, 4], ...]
 * 输入： 4个点在相机1图像中的坐标，以二维列表形式给出，
 *       4个点在相机2图像中的坐标，以二维列表形式给出，
 *       N个相机2图像中坐标的点，以长度为N的二维列表形式给出 
 * 输出： N个相机2图像中坐标的点，以长度为N的二维列表形式给出 
 *       单应矩阵计算完成后，需打印出来
'''
def calc_homography(pts1, pts2, pts_in):
    #
    # code here
    #
    H = []      ## 单应矩阵
    print("Homography")
    print(H)
    pts_out = [[]]  # 输出坐标点，以二维列表返回
    return pts_out

'''
 * Project4: 连通域检测
 * 要求： 
 *  1） 对输入图像进行8-邻接连通域检测，连通域检测不可使用第三方库
 *  2） 输出连通域的数量，并将每个连通域的面积打印，如“连通域1 : 40, 连通域1 : 100”
 *  3） 连通域面积即为连通域中的像素数目
 * 输入图像： Project4.jpg，输入参数为图像名，类型为str
 * 输出： 将连通域面积填充到area中，并且按照从大到小排序，即索引为0的面积最大
 *       返回值以排序后的连通域面积表示，格式为list
 '''
def print_connected_area(in_img_name):
    import cv2
    img     = cv2.imread(in_img_name)
    img     = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    areas   = []
    #
    # code here
    #
    return areas


'''
 * Project5: 计算最小外接矩形
 * 要求： 
 *  1） 给定输入图像，使用project4的方法计算连通域
 *  2） 计算每个连通域的最小外接矩形
 * 注意：题目要求最小外接矩形可能为旋转矩形，矩形可能是长方形或者正方形
 *      即矩形的边不必须是平行坐标轴的        
 * 输入图像： Project5.jpg，输入参数为图像名，类型为str
 * 输出： 将连通域最小外接矩形的面积输出到area中，并且按照从大到小排序，即索引为0的面积最大
 *       返回值以排序后的连通域面积表示，格式为list
'''
def connected_rectangle_area(in_img_name):
    import cv2
    img     = cv2.imread(in_img_name)
    img     = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    areas   = []
    #
    # code here
    #
    return areas


#define MAX_AREA_CNT 1024
if __name__ == '__main__':
    # Project1
    print("========= Project1 =============== \n")
    triangle = [
        [100, 200, 305, 105, 100, 25 ],         # triangle in
        [86,  192, 100, 150, 102, 75 ], 
        [200, 260, 160, 100, 201, 300], 
        [150, 100, 50,  60,  300, 60 ],
        [260, 200, 150, 60,  80,  100]
    ]
    
    for i in range(5):
        for j in range(i+1, 5):
            print("Overlap [%d][%d] : %d"%(i, j, has_overlap(triangle[i], triangle[j])))

    # Project2
    print("\n========= Project2 =============== \n")
    data = [ -32.21, 42.36, -17.66, 46.93, 88.45, -39.05, -7.16, 21.54, 1.85, 3.5, -96.02, 89.63, 50.39, 
            -79.37, 29.27, 73.82, -81.32, 69.24, -46.98, 95.53, -76.9, -52.23, -16.27, 74.15, 13.69, -89.37, 
            26.37, -4.59, 74.6, -29.5, -21.7, 5.82, -50.47, -87.16, 58.73, 14.16, -89.38, 86.33, 32.58, 
            -81.52, 69.85, -16.05, -4.21, -47.58, -86.84, 47.59, -43.65, 99.82, -97.1, 20.21, 9.82, -35.07, 
            96.11, 25.29, -84.58, -78.7, 10.65, 58.65, -59.29, 53.49, 28.44, -25.67, -22.98, 35.67, -8.69, 
            -41.43, -22.29, 48.63, 31.49, 39.87, -86.7, 75.24, 49.47, -1.74, 70.02, -2.42, 41.28, -62.6, 
            -36.29, -4.4, 23.36, -20.06, -54.91, 18.47, 33.65, 86.59, -42.31, -89.57, 21.13, 41.44, -21.17, 
            60.26, -30.71, 0.0, -18.57, 71.01, 31.32, -68.95, -93.25, 27.48  
        ]
    N = 10
    M = 6
    
    avg, var = get_avg_var(data, N, M)
    # Project3
    print("\n========= Project3 =============== \n")
    pts1 = [
        [20, 45],
        [30, 600],
        [560, 650],
        [550, 30]
    ]
    pts2 = [
        [10, 15],
        [400, 560],
        [450, 600],
        [560, 20]
    ]

    pts_in = [
        {15, 25},
        {35, 67},
        {100, 200},
        {300, 560}
    ]
    pts_out = calc_homography(pts1, pts2, pts_in)
    # Project4
    print("\n========= Project4 =============== \n")
    
    areas = print_connected_area("project4.jpg")
    for i in range(len(areas)):
        print("[area %2d]: %.2f" % (i, areas[i]))
    # Project5
    print("\n========= Project5 =============== \n")
    areas = connected_rectangle_area("project4.jpg")
    for i in range(len(areas)):
        print("[area %2d]: %.2f" % (i, areas[i]))
    
    print("\n========= END ==================== \n")

