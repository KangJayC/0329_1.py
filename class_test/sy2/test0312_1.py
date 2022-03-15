def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    list1 = [str(i) for i in array]
    str1=",".join(list1)
    return str1

list_a=eval(input("请输入10个整数："))
print("冒泡排序结果：",bubble_sort(list_a))
