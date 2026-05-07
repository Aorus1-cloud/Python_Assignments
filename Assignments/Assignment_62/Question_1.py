import numpy as np 

def ConvolutionalLayerX(image_matrix,kernel_matrix):
    # matrix.shape = row,column
    row,col = (image_matrix.shape[0] - kernel_matrix.shape[0]) + 1,(image_matrix.shape[1] - kernel_matrix.shape[1]) + 1

    feature_map = [[0 for _ in range(col)] for _ in range(row)]
    
    summ = 0

    for r in range(row):
        for c in range(col):
            for i in range(kernel_matrix.shape[0]):
                for j in range(kernel_matrix.shape[1]):
                    summ = summ + image_matrix[i+r][j+c] * kernel_matrix[i][j]
                    print(f"Position {r},{c} Calculation : {image_matrix[i+r][j+c]} * {kernel_matrix[i][j]} = {summ}")

            feature_map[r][c] = summ
            summ = 0

    return feature_map


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

    feature_map = ConvolutionalLayerX(image,kernel)

    print(feature_map)

if __name__ == "__main__":
    main()