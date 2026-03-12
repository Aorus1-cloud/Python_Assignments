import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def EuclidianDistance(X,Y):
    result = []
    for i in range(len(X)):
        result.append(np.sqrt((X[i]-Y[i])**2))
    
    return result

def main():
    dataset = pd.DataFrame([
        [25,20000],
        [30,40000],
        [35,80000],
    ],
    columns=["A","B"]
    )

    Distance = EuclidianDistance(dataset["A"],dataset["B"])

    print("Distance Without Scaling:")
    for value in Distance:
        print(value)

    scaler = StandardScaler()

    scaled_dataset = pd.DataFrame(scaler.fit_transform(dataset))

    Distance = EuclidianDistance(scaled_dataset[0],scaled_dataset[1])

    print("\nDistance after scaling:")
    for value in Distance:
        print(value)

    print("We can see that distance was biased towards the column 2 when we find the distance without scaling but then after scaling we can conclude that the distance calculation is fare and model trained on such model will be better than the first.")
if __name__ == "__main__":
    main()