import math
x=0
for i in range(100):
    x=(6-x**3-(math.e**x)/2.0)/5.0
    print(str(i)+":"+str(x))