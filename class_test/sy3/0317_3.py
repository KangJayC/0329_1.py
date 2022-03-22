class MyList:  # 定义类MyList
    def __init__(self, *args):  # 构造函数
        self.__mylist = []  # 初始化私有属性，空列表
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, n): # 重载运算符"+"，每个元素增加n
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + n

    def __sub__(self, n):  # 重载运算符"-"，每个元素减少n
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - n

    def __mul__(self, n):  # 重载运算符"*"，每个元素乘以n
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * n

    def __truediv__(self, n):  # 重载运算符"/"，每个元素除以n
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / n

    def __len__(self):  # 对应于内置函数len()，返回列表长度
        return len(self.__mylist)

    def __repr__(self):  # 对应于内置函数str()，显示列表
        # 将__mylist中的元素连接成字符串保存到str1里，即将列表转换成字符串
        list1 = [str(i) for i in self.__mylist]
        str1 = ",".join(list1)
        return str1

#测试代码
m = MyList(1, 2, 3, 4, 5) #创建对象
m + 2; print(repr(m))   #每个元素加2
m - 1; print(repr(m))   #每个元素减1
m * 4; print(repr(m))   #每个元素乘4
m / 2; print(repr(m))   #每个元素除2
print(len(m))         #列表长度

'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''









