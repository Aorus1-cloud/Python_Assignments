import pandas as pd 
import numpy as np

def main():
    mean = 0
    
    dataset = pd.Series([6,7,8,9,10,11,12])

    mean = np.mean(dataset)

    print(mean)

if __name__ == "__main__":
    main()