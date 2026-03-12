import pandas as pd 
import numpy as np 

def StandardScaler(dataset):
    std_deviation = np.std(dataset)
    mean = np.mean(dataset)

    scaled_data = []

    for i in dataset:
        scaled_data.append(((i-mean)/std_deviation))

    scaled_data = pd.Series(scaled_data)

    return scaled_data

def main():
    dataset = pd.DataFrame([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    scaled_dataset = StandardScaler(dataset[1])

    print(scaled_dataset)
    
if __name__ == "__main__":
    main()