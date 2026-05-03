import math,random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def tanh(x):
    return((math.exp(x)-math.exp(-x))/(math.exp(x)+math.exp(-x)))

def relu(x):
    return max(0,x)

def sigmoid(z):
    return (1/(1+math.exp(-z)))


def main():
    # x1 = random.uniform(-10,10)
    # x2 = random.uniform(-10,10)
    # w1 = random.uniform(0,1)
    # w2 = random.uniform(0,1)
    # b = random.uniform(0,1)

    v1 = np.arange(-10,10)

    plt.plot(v1,list(map(sigmoid,v1)),color = "green")
    plt.xlabel("Input Values")
    plt.ylabel("Output")
    plt.axhline(0.5,color='r', linestyle='--', label='Threshold')
    plt.grid(True)
    plt.legend()
    plt.title("Sigmoid")
    plt.show()

    plt.plot(v1,list(map(relu,v1)),color = "green")
    plt.xlabel("Input Values")
    plt.ylabel("Output")
    plt.axvline(x=0,color = "black",label = "Origin")
    plt.grid(True)
    plt.legend()
    plt.title("ReLU")
    plt.show()

    plt.plot(v1,list(map(tanh,v1)),color = "green")
    plt.xlabel("Input Values")
    plt.ylabel("Output")
    plt.axvline(x=0,color = "black")
    plt.axhline(y=0,color = "black",label = "Origin")
    plt.grid(True)
    plt.legend()
    plt.title("Tanh")
    plt.show()

    print("Sigmoid activation function is used in output layer in case of binary classification.")
    print("ReLU is used in hidden layer.")
    print("tanh is used when the input data is +ve and -ve values in case of sigmoid.")
    
if __name__ == "__main__":
    main()