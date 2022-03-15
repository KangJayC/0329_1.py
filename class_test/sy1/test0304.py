import math

def isPrime(num):
  num = int(num)
  if (num <= 3):
    return num > 1
  elif(num % 2 == 0 or num % 3 == 0):
    return False
  elif(num % 6 != 1 and num % 6 != 5):
    return False
  sqrt = int(math.sqrt(num)) + 1
  for i in range(5,sqrt,6):
    if(num % i == 0 or num % (i + 2) == 0):
      return False
  return True

def isReversiblePrime(num):
  num = str(num)
  nums = list(num)
  nums.reverse()
  onum = ''.join(nums)
  if(isPrime(num) and isPrime(onum)):
    return True
  else:
    False

if __name__ == "__main__":
  m = int(input('请输入查找【可逆素数】的开始数：'))
  n = int(input('请输入查找【可逆素数】的结束数：'))
  if(m < n):
    for i in range(m,n):
      if(isReversiblePrime(i)):
        print(i)