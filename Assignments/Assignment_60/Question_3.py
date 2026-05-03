import math,random
def MSE(x,y):
    if len(x) == 1:
        return (x-y)**2
    
    else:
        res = 0

        for i,j in zip(x,y):
            res = res + (i-j)**2

        res = res / len(x)

        return res
    
def BCE(y_t,y_p):
    if len(y_t) == 1:
        return ((y_t*math.log(y_p))+((1-y_t)*math.log(1-y_p)))
    
    else:
        res = 0
        epsilon = 1e-15  # Tiny value to prevent log(0)

        for i,j in zip(y_t,y_p):

            j = max(epsilon, min(1 - epsilon, j))       # To prevent log(0) and log(1-1)

            res = res + ((i*math.log(j))+((1-i)*math.log(1-j)))

        res = -res/len(y_t)

        return res


def main():
    Y_test = [1,2,3,4,5,6]
    Y_pred = [2,4,6,5,4,3]

    res = MSE(Y_test,Y_pred)
    print("The MSE of the y_test and y_pred is :",res)

    Y_test = [random.randint(0,1) for _ in range(5)]
    Y_pred = [random.randint(0,1) for _ in range(5)]

    res = BCE(Y_test,Y_pred)

    print("The binary_crossentropy of the y_test and y_pred is :",res)

    print("Binary Cross Entropy is used in case binary classification and the mse is used in case of regression.")

if __name__ == "__main__":
    main()