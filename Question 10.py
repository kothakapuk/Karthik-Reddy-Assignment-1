import numpy
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from collections import Counter
import numpy as np





# creating an array to understand its attributes
a = np.array([1,2,3,6,6,7,10,11])
y = np.array([0,0,1,1,1,0,0,0])




x_train,x_test,y_train,y_test=train_test_split(a,y,test_size=0.5,random_state=4,stratify = y)
x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)
print(x_train,x_test,y_train,y_test)





def KNN(x,y,k,z):
    dist = []
    # Computing Euclidean distance
    dist_ind = np.sqrt(np.sum((x-y)**2, axis=1))
    print(dist_ind)
    # Concatinating the label with the distance
    main_arr = np.column_stack((z,dist_ind))
    print(main_arr)
    # Sorting the distance in ascending order
    main = main_arr[main_arr[:,1].argsort()]
    # Calculating the frequency of the labels based on value of K
    count = Counter(main[0:k,0])
    keys, vals = list(count.keys()), list(count.values())
    if len(vals)>1:
        if vals[0]>vals[1]:
            return int(keys[0])
        else:
            return int(keys[1])
    else:
        return int(keys[0])





k=3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train,y_train)
yprediction = knn.predict(x_test)
print("accuracy= ",accuracy_score(y_test,yprediction))




for i in x_test:
    result = KNN(x_train,i,3,y_train)
    print(result)





print(y_test,yprediction)



