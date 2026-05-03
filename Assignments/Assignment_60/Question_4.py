import math

def sigmoidDerivative(x):
    return x*(1 - x)

def sigmoid(z):
    return(1/(1+math.exp(-z)))

def SinglePerceptron(X1,X2,W1,W2,B):
    weighted_sum = 0
    output = 0

    weighted_sum = (X1*W1)+(X2*W2)+B

    output = sigmoid(weighted_sum)

    return output

def weightUpdate(x1,x2,ytest,ypred,w1,w2,bias):
    learning_rate = 0.1

    loss = 0.5 * (ytest - ypred) ** 2  # Calculating Loss
    '''
    We cant directly calculate how much loss changes with change in w1,w2,b
    so we approach with a step by step method which is like
    we find dL/doutput which gives us change in loss with change in output 
    and then we will find doutput/dz which will give us how much output changes with change in z value 
    so by chain rule we can find 
    change in loss with respect to change in z value which will help us in updating the weight with according to the output
    
    '''
    dL_doutput = ypred - ytest               # This gives us how much loss changes with change in output
    doutput_dz = sigmoidDerivative(ypred)    # This give us the change in output with respect to change in value of dz

    # By chain rule
    dL_dz = dL_doutput * doutput_dz 

    dL_dw1 = x1 * dL_dz
    dL_dw2 = x2 * dL_dz
    dL_db = dL_dz

    # Gradient Descent 
    # Updating weights and bias
    w1 = w1 - (learning_rate * dL_dw1)
    w2 = w2 - (learning_rate * dL_dw2)
    bias = bias - (learning_rate * dL_db)

    return w1,w2,bias


def main():
    x1 = 2
    x2 = 3
    w1 = 0.4
    w2 = 0.6
    bias = 0.5
    y_test = 7

    y_pred = SinglePerceptron(x1,x2,w1,w2,bias)

    w1,w2,bias = weightUpdate(x1,x2,y_test,y_pred,w1,w2,bias)

    print(f"Old w1 : 0.4 , New Weight : {w1}")
    print(f"Old weight w2 : 0.6,New weight : {w2}")
    print(f"Old bias : 0.5,New bias :{bias}")

if __name__ == "__main__":
    main()