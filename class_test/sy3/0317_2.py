class Temperature:
  def __init__(self,degree): #构造函数
    self.degree=degree
  def ToFahrenheit(degree):
    degree = float(degree)
    degree1 = (degree * 9/5) + 32
    return degree1
  def ToCelsius(degree1):
    degree1 = float(degree1)
    degree = (degree1 - 32) * 5 /9
    return degree
degree=float(input("请输入摄氏温度:"))
ToFahrenheit=Temperature.ToFahrenheit(degree)
print("摄氏温度={0}，华氏温度={1}".format(degree,ToFahrenheit))
degree1=float(input("请输入华氏温度:"))
ToCelsius=Temperature.ToCelsius(degree1)
print("华氏温度={0}，摄氏温度={1}".format(degree1,ToCelsius))
