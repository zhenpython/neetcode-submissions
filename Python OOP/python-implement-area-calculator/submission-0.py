import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        self.length = length
        self.width = width
        if self.width == None:
            result = math.pi*(self.length**2)
            result = round(result, 2)
            return result
        else:
            return self.length * self.width

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
