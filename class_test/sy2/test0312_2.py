def selection_sort(array):
     for i in range(len(array) - 1):
         min_index = i
         for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
               min_index = j
         array[min_index], array[i] = array[i], array[min_index]
     list1 = [str(i) for i in array]
     str1 = ",".join(list1)
     return str1


list_a = eval(input("请输入10个整数："))
print("选择排序结果：", selection_sort(list_a))