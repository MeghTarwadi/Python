import numpy


# ar=numpy.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])

# # print(ar[2])


ar=numpy.array([[[1,2,3],[4,5,6]]])

numpy.savetxt('opfile.txt',ar)

a=load('opfile.txt')
# print(ar.shape)
# print("dime",ar.ndim)
# print(ar)

