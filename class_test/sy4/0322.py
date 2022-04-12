class Color:
    def __init__ (self,r=0,g=0,b=0):
        self._r=r#Red红色分量
        self._g=g#Green绿色分量
        self._b=b#Blue蓝色分量
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
        return .299*self.r+.587*self.g+.114*self.b

    def toGray(self):
        y= int(round(self.luminance()))
        return Color(y,y,y)


    def isCompatible(self,c):
        return abs(self.luminance()-c.luminance())>=128.0

    def __str__ (self):
        return '({},{},{})'.format(self._r,self._g,self._b)



WHITE=Color(255,255,255)
BLACK=Color(0,0,0)
RED=Color(255,0,0)
GREEN=Color(0,255,0)
BLUE=Color(0,0,255)
CYAN=Color(0,255,255)
MAGENTA =Color(255,0,255)
YELLOW=Color(255,255,0)

if __name__=='__main__':
    c=Color(255,200,0)#ORANGE(橙色)
    print('颜色字符串：{}'.format(c))#输出颜色字符串
    print('颜色分量：r={},g={},b={}'.format(c.r,c.g,c.b))#输出个颜色分量
    print('颜色亮度：{}'.format(c.luminance()))#输出颜色亮度
    print('转换为幅度颜色：{}'.format(c.toGray()))#输出转换后的灰度颜色
    print('{}和{}是否匹配：{}'.format(c,RED,c.isCompatible(RED)))#比较与红色是否匹配