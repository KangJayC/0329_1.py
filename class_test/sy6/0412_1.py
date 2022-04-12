class Teacher(1):
    def __init__(self, name="", age=30, sex="man", department="Computer"):
        # 调用基类构造方法初始化基类的私有数据成员
        super(Teacher, self).__init__(name, age, sex)
        # 调用方法对工作部门进行初始化
        2


def setDepartment(self, department):
    if type(department) != str:
        raise Exception("department must be a string")
    self.__department = 3


# 重写从父类中继承来的方法
def show(self):
    # 先调用父类的同名方法，显示从父类中继承来的数据成员
    super(Teacher, self).show()
    # 再显示派生类中的私有数据成员
    print(4)


if __name__ == "__main()__":
    # 创建基类对象
    zl = Person("张丽", 18, "woman")
    zl.show()
    print("=" * 30)

    # 创建派生类对象
    wxr = Teacher("王校荣", 32, "man", "Math")
    wxr.show()
    # 调用继承的方法修改年龄为35
    5
wxr.show()
