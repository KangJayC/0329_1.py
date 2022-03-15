import math
class MyMath:
  def C(self,r):
    return 2*math.pi*r
  def S(self,r):
    return math.pi*r*r
  def sphere_S(self,r):
    return 4*math.pi*r*r
  def sphere_V(self,r):
    return 4/3*math.pi*math.pow(r,3)

X=MyMath()
R=float(input("请输入半径:"))
print("圆的周长={:.2f}".format(X.C(R)))
print("圆的面积={:.2f}".format(X.S(R)))
print("球的表面积={:.2f}".format(X.sphere_S(R)))
print("球的体积={:.2f}".format(X.sphere_V(R)))
