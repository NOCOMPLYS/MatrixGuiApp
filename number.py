from rational import TRational

class number():
    
    def __init__(self, divisible, divisor):
        self.value = TRational(divisible, divisor)