import numpy as np

def Flattening(input):
    Flatten_matrix = [0 for _ in range(input.shape[0]+input.shape[1])]
    
    index = 0

    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            Flatten_matrix[index] = input[i][j]
            index+=1
            
    return Flatten_matrix

def main():
    matrix = [
    [6, 4],
    [8, 6]
    ]

    flatten_matrix = Flattening(np.array(matrix))

    print("The flatten output of the input matrix is :\n",flatten_matrix)

if __name__ == "__main__":
    main()