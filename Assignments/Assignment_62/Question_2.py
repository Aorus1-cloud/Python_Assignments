import numpy as np 
import math


# padding logic addinng to the pooling matrix shape identification remaining

def ConvolutionalLayerX(image_matrix,kernel_matrix):
    h,w = image_matrix.shape[0],image_matrix.shape[1]

    # return 1 if odd and 0 if even
    pad_h = h % 2
    pad_w = w % 2
                   # np.pad(array,((top,bottom),(left,right)),mode)
    image_matrix = np.pad(image_matrix,((0,pad_h),(0,pad_w)),mode="constant")

    # print(f"Input matrix shape after padding : {image_matrix.shape}")

    # matrix.shape = row,column
    row,col = (image_matrix.shape[0] - kernel_matrix.shape[0]) + 1,(image_matrix.shape[1] - kernel_matrix.shape[1]) + 1

    feature_map = [[0 for _ in range(col)] for _ in range(row)]
    
    summ = 0

    for r in range(row):
        for c in range(col):
            for i in range(kernel_matrix.shape[0]):
                for j in range(kernel_matrix.shape[1]):
                    summ = summ + image_matrix[i+r][j+c] * kernel_matrix[i][j]
                    # print(f"Position {r},{c} Calculation : {image_matrix[i+r][j+c]} * {kernel_matrix[i][j]} = {summ}")

            feature_map[r][c] = summ
            summ = 0

    return np.array(feature_map),pad_h+pad_w

def ReLUX(input_matrix):
    output = [[0 for _ in range(input_matrix.shape[1])] for j in range(input_matrix.shape[0])]

    for i in range(input_matrix.shape[0]):
        for j in range(input_matrix.shape[1]):
            output[i][j] = max(0,input_matrix[i][j])

    return np.array(output)

def MaxPoolingX(input_matrix,padding):
    maxpooler_shape = 2
    maximum = 0
    stride_row = 0
    stride_col = 0
    pooling_output = np.array([[0 for i in range((math.floor((input_matrix.shape[1]-maxpooler_shape)/maxpooler_shape))+1)] for j in range((math.floor((input_matrix.shape[0]-maxpooler_shape)/maxpooler_shape))+1)])


    while stride_row < input_matrix.shape[0]:
        x,z = 0,0
        for i in range(maxpooler_shape):
            for j in range(maxpooler_shape):
                maximum = max(maximum,input_matrix[i+stride_row][j+stride_col])
                pooling_output[x][z]= maximum
                z+=1
                if z == pooling_output.shape[1]:
                    z = 0
                    x+=1

            stride_col += maxpooler_shape
            if stride_col >= input_matrix.shape[1]:
                stride_row += maxpooler_shape
                stride_col = 0

    return pooling_output

def main():
    image =np.array( [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ])
        
    kernel = np.array([
    [-1, -1, -1],
    [ 0, 0, 0],
    [ 1, 1, 1]
    ])

    feature_map,padding_size = ConvolutionalLayerX(image,kernel)

    ReLU_output = ReLUX(feature_map)

    final_output = MaxPoolingX(ReLU_output,padding_size)

    print("Output after Pooling : \n",final_output)
    print("pooling reduces size bcz it extract the features from a windows and reduces it to a single value with reduces the overall size of the output matrix.")

if __name__ == "__main__":
    main()