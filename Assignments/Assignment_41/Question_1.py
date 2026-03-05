from math import sqrt

def EuclidianDistanceX(X_train,Y_train,X_test,Y_test):
    return sqrt(((X_test-X_train)**2) + ((Y_test-Y_train) **2))

def main():
    Border = "-"*40

    print(Border)
    print("---------- KNearestNeighbourX ----------")
    print(Border)

    dataset = [
        {'Point':'A','X':1,'Y':2,'Label':"Red"},
        {'Point':'B','X':2,'Y':3,'Label':"Red"},
        {'Point':'C','X':3,'Y':1,'Label':"Blue"},
        {'Point':'D','X':6,'Y':5,'Label':"Blue"},
              ]
    
    X_test = int(input("Enter the X coordinate of new point :"))
    Y_test = int(input("Enter the Y coordinate of new point :"))

    for i in range(len(dataset)):
        dataset[i]['distance'] = EuclidianDistanceX(X_train=dataset[i]['X'],X_test=X_test,Y_train=dataset[i]['Y'],Y_test=Y_test)

    sorted_dataset = sorted(dataset,key=lambda x : x['distance'])
    
    # print(f"What should be the value of k(below or equal to {20/100*5} and keep it odd) :")
    # k = int(input())

    k = 3

    sorted_dataset = sorted_dataset[:k]
    print("Nearest Neighbours :")
    for f in sorted_dataset:
        print(f)

    result = {}

    for i in sorted_dataset:
        if i['Label'] not in result:
            result[f'{i['Label']}'] = 1
        else:
            result[f'{i['Label']}'] = result[f'{i['Label']}'] + 1

    print("The predicted class of new point is :",max(result,key=result.get))


if __name__ == "__main__":
    main()

