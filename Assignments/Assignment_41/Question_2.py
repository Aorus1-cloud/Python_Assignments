import pandas as pd

class KNearestNeighbour2Dx:
    import pandas as pd
    from math import sqrt

    def __init__(self,k=3):
        if type(k) != int:
            print("K must be an integer.")
            return

        self.k = int(k) 
    
    def fit(self,X,y):
        self.X = X
        self.y = y

    def predict(self,X_test,Y_test):

        for i in range(len(self.X)):
            self.X.loc[i,'distance'] = self.EuclidianDistanceX(X1_train=self.X.iloc[i,0],X2_train=self.X.iloc[i,1],X1_test=X_test,X2_test=Y_test)

        result = pd.concat([self.X,self.y],axis=1)

        sorted_result = result.sort_values(by=['distance'])

        sorted_result = sorted_result[:self.k]

        class_count = {}

        for i in range(len(sorted_result)):
            if sorted_result.iloc[i,3] not in class_count:

                class_count[f'{sorted_result.iloc[i,3]}'] = 1

            else:
                class_count[f'{sorted_result.iloc[i,3]}'] += 1

        return max(class_count,key=class_count.get)


    def EuclidianDistanceX(self,X1_train,X2_train,X1_test,X2_test):
        return self.sqrt(((X1_test-X1_train)**2) + ((X2_test-X2_train) **2))

def main():
    Border = "-"*40

    print(Border)
    print("---------- KNearestNeighbourX ----------")
    print(Border)
    
    df = pd.DataFrame([
    {'Point':'A','X':1,'Y':2,'Label':"Red"},
    {'Point':'B','X':2,'Y':3,'Label':"Red"},
    {'Point':'C','X':3,'Y':1,'Label':"Blue"},
    {'Point':'D','X':6,'Y':5,'Label':"Blue"},
            ])
    
    X_train = df[['X','Y']]
    Y_train = df[['Label']]

    X_test = int(input("Enter the X coordinate of new point :"))
    Y_test = int(input("Enter the Y coordinate of new point :"))

    model_k1 = KNearestNeighbour2Dx(k = 1)
    model_k3 = KNearestNeighbour2Dx(k = 3)
    model_k5 = KNearestNeighbour2Dx(k = 5)

    model_k1.fit(X_train,Y_train)
    model_k3.fit(X_train,Y_train)
    model_k5.fit(X_train,Y_train)

    result1 = model_k1.predict(X_test=X_test,Y_test=Y_test)
    result3 = model_k3.predict(X_test=X_test,Y_test=Y_test)
    result5 = model_k5.predict(X_test=X_test,Y_test=Y_test)

    print(f"K = 1 -> {result1}")
    print(f"K = 3 -> {result3}") 
    print(f"K = 5 -> {result5}")

    '''
        The predicted output changes with change in k value because the nearest neighbours increase
        with increase in k value so it needs to vote for more value and the output
        becomes precise therefore,
        the output changes with change in k value 
    '''

if __name__ == "__main__":
    main()







