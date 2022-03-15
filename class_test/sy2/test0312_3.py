def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    list1 = [str(i) for i in arr]
    str1 = ",".join(list1)
    return str1


list_a = eval(input("请输入10个整数："))
print("插入排序结果：", insertion_sort(list_a))