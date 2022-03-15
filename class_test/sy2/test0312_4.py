
def binarySearch(key,a,lo,hi):
   if hi<=lo:
       return "目标没有找到！"
   mid=(lo+hi)//2
   if a[mid]>key:
       return binarySearch(key,a,lo,mid)
   elif a[mid]<key:
       return binarySearch(key,a,mid,hi)
   else:
       return mid+1

ls=eval(input("请输入10个整数："))
target=eval(input("请输入目标："))
print("目标的序号是",binarySearch(target,ls,0,len(ls)-1))