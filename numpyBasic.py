
import numpy

speed = [99,23,23,44,53,56,78,46,36,36,7,8,223,4,55,89]
x = numpy.mean(speed)
print("the mean is " + str(x))

y = numpy.median(speed)
print("the median is " + str(y))

z = numpy.std(speed)
print("the standard devation is " + str(z))
xy = numpy.var(speed)
print("the variance is " + str(xy))