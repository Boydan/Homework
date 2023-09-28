import math
from math import sqrt
class Complex:
    @staticmethod
    def _incomplex(n):
        if isinstance(n,(int, float)) :
            n=Complex(n)
            return n
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Complex' and '{type(other).__name__}'")
    def __init__(self, re=0, img=0):
        self.re = re
        self.img = img
    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self.re + other.re, self.img + other.img)
        else:
            other=self._incomplex(other)
            return Complex(self.re + other.re, self.img + other.img)

    def __sub__(self, other):
        if isinstance(other,Complex):
            return Complex(self.re - other.re, self.img - other.img)
        else:
            other=self._incomplex(other)
            return Complex(self.re - other.re, self.img - other.img)

    def __mul__(self, other):
        if isinstance(other,Complex):
            return Complex((self.re * other.re)-(self.img * other.img), (self.re*other.img)+(self.img*other.re))
        else:
            other=self._incomplex(other)
            return Complex((self.re * other.re)-(self.img * other.img), (self.re*other.img)+(self.img*other.re))
    def __truediv__(self, other):
        if isinstance(other,Complex):
            lag=((self.re*other.re)+(other.img*self.img))/(other.re*other.re+other.img*other.img);
            lag2=((self.img*other.re)-(self.re*other.img))/(other.re*other.re+other.img*other.img);
            return Complex(lag,lag2)
        else:
            other=self._incomplex(other)
            lag=((self.re*other.re)+(other.img*self.img))/(other.re*other.re+other.img*other.img);
            lag2=((self.img*other.re)-(self.re*other.img))/(other.re*other.re+other.img*other.img);
            return Complex(lag,lag2)

    def __abs__(self):
        new = (self.re**2 + (self.img**2))**(0.5)
        return new
    def __repr__(self):
        wtf="Complex(%.2f,%.2f)"% (self.re, self.img)
        return wtf

    def __str__(self):
        if self.img == 0:
            result = "%.2f+0.00i" % (self.re)
        elif self.re == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % (self.img)
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img > 0:
            result = "%.2f+%.2fi" % (self.re, self.img)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.img))
        return result
c1=Complex(3,-7)
c2=Complex(4,8)
print(c1+c2)
print(c1+2)

print(c1+"321")
