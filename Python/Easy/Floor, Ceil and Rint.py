import numpy
numpy.set_printoptions(sign=' ')

arr = numpy.array(input().split(' '),dtype=float)
print(str(numpy.floor(arr)))
print(str(numpy.ceil(arr)))
print(str(numpy.rint(arr)))
