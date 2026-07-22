# import numpy as np

# arr = np.array([1,2,3,4,5])

# print(arr)
#import = import libeary
#numpy = libeary
#as np = alias short name
# example numpy
# import numpy as np

# arr = np.array([1,2,3,4,5,6,7])
# print(arr*2)
#creating array
#1D
# import numpy as np
# arr =np.array([1,6,7,8,9])
# print(arr)
#2D
# import numpy as np
# arr = np.array([[1,2,3,4],[0,7,5,4]])
# print(arr)
#3D
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)

# import numpy as np
# arr =np.zeros((2,3))

# arr=np.ones((3,3))

# arr =np.empty((2,2))

# arr =np.eye(4)

# arr =np.full((2,2),5)

# arr = np.arange(1,11)

# arr =np.arange(2,10,2)

# arr = np.linspace(1,100,5)


# print(arr)


#indexing
# import numpy as np

# arr =np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[1])

#scling 
# print(arr[1:4])


#2D array indexing

# import numpy  as np

# arr =np.array([[1,2,3],
#                [4,5,6]
#                ])
# print(arr[0,1])
# print(arr[1,2])

#mathamthical opretion(broadcasting)
# import  numpy as np
# arr =np.array([1,2,3,4,5,6,7])
# print(arr+2)
# print(arr-1)
# print(arr*3)
# print(arr/2)
# print(arr**2)

# statical function
# import  numpy as np
# arr =np.array([10,20,30,40])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.max(arr))
# print(np.min(arr))
# print(np.std(arr))
# print(np.var(arr))

#reshap
# import  numpy as np
# arr =np.array([10,20,30,40])
# print(arr.reshape((2,2)))

#Flatten
# arr = np.array([[1,3],[4,5]])
# print(arr.flatten())

# print(np.random.rand(5))
# print(np.random.randint(1,100,5))
#sorting
# arr =np.array([100,401,313,204])
# print(np.sort(arr))

#Copy() and view()

# import numpy as np
# arr = np.array([1,2,5,4])

# copy =arr.copy()
# copy[0]=100
# print(arr)
# print(copy)


# import numpy as np
# arr = np.array([1,2,5,4])

# view =arr.view()
# view[0]=100
# print(arr)
# print(view)