

class TRational():

    def __reduction(self):
        gcd = self.gcd_func(self.__divisible, self.__divisor)
        self.__divisible /= gcd
        self.__divisor /= gcd
        self.__divisible = int(self.__divisible)
        self.__divisor = int(self.__divisor)
        self.text_representation = f'{self.__divisible}/{self.__divisor}'

    def __init__(self, divisible, divisor):
        self.__divisible = divisible
        self.__divisor = divisor
        self.text_representation = f'{self.__divisible}/{self.__divisor}'
        if self.__divisible != 0 and self.__divisor != 0:
            self.__reduction()
    
    def gcd_func(self, x, y): 
        if(y == 0): 
            return x
        else: 
            return self.gcd_func(y, x % y)
    
    def lcm_func(self, x, y): 
        if x > y:
            greater = x
        else: 
            greater = y 
        while(True): 
            if((greater % x == 0) and(greater % y == 0)): 
                lcm = greater 
                break 
            greater += 1 
        return lcm

    def __bringing(self, other, lcm):
        int_part = int(lcm / self.__divisor)
        self.__divisor = int_part * self.__divisor
        self.__divisible = int_part * self.__divisible
        self.text_representation = f'{self.__divisible}/{self.__divisor}'
        int_part = int(lcm / other.__divisor)
        divisor = other.__divisor * int_part
        divisible = other.__divisible * int_part
        return [divisible, divisor]


    def __add__(self, other):
        if isinstance(other, int):
            result = TRational(self.__divisible + self.__divisor * other, self.__divisor)
            result.__reduction()
            return result
        elif isinstance(other, TRational):
            if self.__divisor == other.__divisor:
                result = TRational(self.__divisible + other.__divisible, self.__divisor)
                result.__reduction()
                return result
            else:
                lcm  = self.lcm_func(self.__divisor, other.__divisor)
                new = self.__bringing(other, lcm)
                result = TRational(self.__divisible + new[0], lcm)
                result.__reduction()
                return result

    def __sub__(self, other):
        if isinstance(other, int):
            result = TRational(self.__divisible - self.__divisor * other, self.__divisor)
            result.__reduction()
            return result
        elif isinstance(other, TRational):
            if self.__divisor == other.__divisor:
                result = TRational(self.__divisible - other.__divisible, self.__divisor)
                result.__reduction()
                return result
            else:
                lcm = self.lcm_func(self.__divisor, other.__divisor)
                new = self.__bringing(other, lcm)
                result = TRational(self.__divisible - new[0], lcm)
                result.__reduction()
                return result
    
    def __mul__(self, other):
        if isinstance(other, int):
            result = TRational(self.__divisible * other, self.__divisor)
            result.__reduction()
            return result
        elif isinstance(other, TRational):
            result = TRational(self.__divisible * other.__divisible, self.__divisor * other.__divisor)
            result.__reduction()
            return result

    def __truediv__(self, other):
        if isinstance(other, int):
            result = TRational(self.__divisible, self.__divisor * other)
            result.__reduction()
            return result
        elif isinstance(other, TRational):
            result = TRational(self.__divisible * other.__divisor, self.__divisor * other.__divisible)
            result.__reduction()
            return result
