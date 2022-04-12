class Test:
    def __init__(self,value):
        self.__value=value

    @property
    def value(self):  #只读属性，无法对它进行修改和删除
         return self.__value

    @value.setter
    def value(self,value):
        self.__value=value

    @value.deleter
    def value(self,value):
        del self.__value

test1=Test(100)
print("数值是：",test1.value)
test1.value=90
print("数值是：",test1.value)
del test1.value
print("数值是：",test1.value)




