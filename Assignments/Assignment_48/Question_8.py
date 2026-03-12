import pandas as pd
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

def ConfusionMatrix(Y_test,Y_pred):
    TP = 0
    TN = 0
    FP = 0 
    FN = 0

    for i in range(len(Y_test)):
        if Y_test[i] == 1:
            if Y_test[i] == Y_pred[i]:
                TP+=1
            else:
                FN+=1
        else:
            if Y_test[i] == Y_pred[i]:
                TN+=1
            else:
                FP+=1

    cm = pd.DataFrame(data=([TP,FN],[FP,TN]),columns=["POSITIVE","NEGATIVE"],index=["POSITIVE","NEGATIVE"])

    return cm

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    print("The confusion Matrix of the output will be as \n",ConfusionMatrix(actual,predicted))
    
if __name__ == "__main__":
    main()