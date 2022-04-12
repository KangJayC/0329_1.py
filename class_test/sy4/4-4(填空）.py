class Color:
    def __init__(self,r=0,g=0,b=0):
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r
    @property
    def g(self):
        return self._g
    @property
    def b(self):
        return self._b

    def luminance(self):
        return 0.299 * self.r + 0.587 * self.g + 0.114 * self.b

    def toGray(self):
        y = int(round(self.luminance()))
        return Color(y, y, y)

    def isCompatible(self,c):
         return abs(self.luminance() - c.luminance()) >= 128.0

    def __str__(self):
        return '({},{},{})'.format(self._r,self._g,self._b)

RED=Color(255,0,0)

if __name__=='__main__':
  c=Color(255,200,0)    #orange
  print('颜色字符串:{}'.format(c))
  print('颜色分量:r={},g={},b={}'.format( c.r,c.g,c.b ))
  print('颜色亮度:{}'.format( c.luminance() ))
  print('转换为灰度颜色:{}'.format(c.toGray()))
  print('{}和{}是否兼容：{}'.format( c,RED,c.isCompatible(RED)))
  
  
  

      


        
