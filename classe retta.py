Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Retta:


    def _init_(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__punti = []

        
        if (self._a, self._b) == (0.0, 0.0):
            raise Exception(f"{self.eq_implicita()} non è una retta")
        
        self._m = - self.a / self._b
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c

    def get_m(self):
        return self.__m

    def trova_y(self, x):
        y = int((self._m * x) + self._c)
        self.__punti.append((x, sy))
        return y

    def eq_implicita(self):
        return f"{self._a}X + {self.b}Y + {self._b} = 0"

    def eq_esplicita(self):
        return f"Y = {self._m}X + {self.c/self._b}"