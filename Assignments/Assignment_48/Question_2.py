import pandas as pd 
import numpy as np
from functools import reduce

def variance(dataset):
    mean = np.mean(dataset)

    deviation = []

    for i in dataset:
        deviation.append(i - mean)

    deviation = pd.Series(deviation)

    deviation_sqr = deviation.apply(lambda x : x**2)

    summ_deviation_sqr = reduce(lambda x,y : x+y,deviation_sqr)

    variance = summ_deviation_sqr/len(dataset)

    return variance

def main():
    mean = 0
    
    dataset = pd.Series([6,7,8,9,10,11,12])

    var = variance(dataset=dataset)

    print("variance of the dataset is :",var)
    print("standard deviation of the dataset is :",np.sqrt(var))

if __name__ == "__main__":
    main()