from Question_1 import LinearRegression2dX
import pandas as pd
from sklearn.metrics import mean_squared_error

def MeanSquaredError(Y_test,Y_pred,show_intermediate = False):
    n = len(Y_test)
    numerator = 0

    for i in range(n):
        numerator = numerator + ((Y_test[i] - Y_pred[i]) ** 2)

        if show_intermediate:
            Border = "-"*40
            print(Border+"\n")
            print("--------- Mean Squared Error -----------\n")
            print(Border+"\n")
            print(f"({Y_test[i]} - {Y_pred[i]}) ** 2 = {numerator}")

    mean_squared_error = numerator / n

    if show_intermediate:
        print("The value of n is :",n)
        print(f"mean_squared_error is : {numerator} / {n}")
        print(f"{mean_squared_error}")

    return mean_squared_error


def R2(Y_test,Y_pred,show_intermediate = False):
    y_mean = Y_test.mean()

    numerator = 0
    denominator = 0

    for i in range(len(Y_test)):
        numerator = numerator + ((Y_pred[i]-y_mean) ** 2)
        denominator = denominator + ((Y_test[i]-y_mean)** 2)

        if show_intermediate:
            Border = "-"*40
            print(Border+"\n")
            print("----------- R2 Calculation -------------\n")
            print(Border+"\n")

            print(f"Numerator : ({Y_pred[i]}-{y_mean}) ** 2 = {numerator}")
            print(f"Denominator :({Y_test[i]}-{y_mean}) ** 2 = {denominator}")

    if show_intermediate:
        print(f"r2 = {numerator} / {denominator}")

    r2 = numerator / denominator

    return r2


def main():
    X = pd.Series([1,2,3,4,5])
    y = pd.Series([3,4,2,4,5])

    model = LinearRegression2dX()

    model.fit(X,y)


    res = model.predict(y)

    r2_score = R2(Y_test=y,Y_pred=res,show_intermediate=True)
    mean_sqr_error = MeanSquaredError(Y_test=y,Y_pred=res,show_intermediate=True)

    print(f"r2 score of the model is :{r2_score:.2f}")
    print(f"The mean_squared_error is : {mean_sqr_error:.2f}")
    
if __name__ == "__main__":
    main()