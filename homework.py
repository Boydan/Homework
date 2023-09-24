import math
from math import sqrt
class Complex:
    def __init__(self, re=0, img=0):
        self.re = re
        self.img = img

    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self.re + other.re, self.img + other.img)
        else:
            return Complex(self.re+other,self.img)

    def __sub__(self, other):
        if isinstance(other,Complex):
            return Complex(self.re + other.re, self.img + other.img)
        else:
            return Complex(self.re-other,self.img)

    def __mul__(self, other):
        if isinstance(other,Complex):
            return Complex((self.re * other.re)-(self.img * other.img), (self.re*other.img)+(self.img*other.re))
        else:
            return Complex(self.re*other,self.img*other)
    def __truediv__(self, other):
        if isinstance(other,Complex):
            lag=((self.re*other.re)+(other.img*self.img))/(other.re*other.re+other.img*other.img);
            lag2=((self.img*other.re)-(self.re*other.img))/(other.re*other.re+other.img*other.img);
            return Complex(lag,lag2)
        else:
            return Complex(self.re/other,self.img/other)

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

