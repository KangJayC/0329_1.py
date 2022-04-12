class Person(object):
    def __init__(self,name='',age=20,sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self,name):
        if not isinstance(name,str):
            raise Exception("name must be string.")
        self.__name=name

    def setAge(self,age):
        if type(age)!=int:
            raise Exception("age must be integer.")
        self.__age=age

    def setSex(self,sex):
        if sex not in("man","woman"):
            raise Exception("sex must be 'man' or 'woman'")
        self.__sex=sex

    def show(self):
        print(self.__name,self.__age,self.__sex,sep='\n')


class Teacher(Person):
     def __init__(self,name="",age=30,sex="man",department="Computer"):
        #调用基类构造方法初始化基类的私有数据成员
        super(Teacher,self).__init__(name,age,sex)
        #调用方法对工作部门进行初始化
        #self.setDepartment=department***********************************************错误！！！！！！！！！！
        self.setDepartment(department)


     def setDepartment(self,department):
        if type(department)!=str:
            raise Exception("department must be a string")
        self.__department=department
    #重写从父类中继承来的方法


     def show(self):
         #先调用父类的同名方法，显示从父类中继承来的数据成员
          super(Teacher,self).show()
          #再显示派生类中的私有数据成员
          print(self.__department)

if __name__=="__main__":
    #创建基类对象
    zl=Person("张丽",18,"woman")
    zl.show()
    print("="*30)

    #创建派生类对象
    wxr=Teacher("王校荣",32,"man","Math")
    wxr.show()
    #调用继承的方法修改年龄为35
    wxr.setAge(35)
    wxr.show()
