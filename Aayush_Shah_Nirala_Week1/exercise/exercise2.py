import math
a = 9
b = 8
c = 12
d = 33
e = 5
N = 5
sum = (a + b + c + d + e)
print(sum)
mean = (a + b + c + d + e)/N
print(mean)

sd = math.sqrt(((a - mean)**2 +
                (b - mean)**2 +
                (c - mean)**2 +
                (d - mean)**2 +
                (e - mean)**2)/N)

print(sd)




















