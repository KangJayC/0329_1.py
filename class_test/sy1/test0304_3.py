import math

def isPrime(n):
  if n <= 1:
    return 0
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
       return 0
    return 1


if __name__=="__main__":
   count = 0

for a in range(1, 9+1):
   for b in range(0, 9+1):
      for c in range(0, 9+1):
         for d in range(1, 9+1):
             if isPrime(a*1000+b*100+c*10+d):
                if isPrime(a+b*10+c*100+d*1000):
                    if count % 15 == 0:
                        print()
                    print("%d " %(a*1000+b*100+c*10+d), end="")
                    count += 1

print("\n4位可逆素数共有%d个" %count)

