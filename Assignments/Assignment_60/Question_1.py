import math

def sigmoid(z):
    return(1/(1+math.exp(-z)))

def SinglePerceptron(X1,X2,W1,W2,B):
    weighted_sum = 0
    output = 0

    weighted_sum = (X1*W1)+(X2*W2)+B

    output = sigmoid(weighted_sum)

    return output

def main():
    x1 = 2
    x2 = 3
    w1 = 0.4
    w2 = 0.6
    bias = 0.5

    y_pred = SinglePerceptron(x1,x2,w1,w2,bias)

    print("Predicted output of the single neuron is :",y_pred)
    print("The output is closer to 1!")
if __name__ == "__main__":
    main()