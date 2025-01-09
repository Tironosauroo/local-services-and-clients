import math
class Calculator:
    # input - list of ints.
    def __init__(self, input, tolerance=1e-10):
        self.input = input 
        self.tolerance = tolerance
        self.angle_degrees = input[0]
        self.angle_radians = math.radians(input[0])
        # input() 

    def add(self):
        total = 0
        for num in self.input:
            total += num #total = total+num
        return total
    def subtract(self):
        total = self.input[0]  # Перший елемент як початкова сума
        for num in self.input[1:]:  # Проходимо через решту елементів
            total -= num
        return total
    def mul(self):
        result = 1  # Початкове значення для множення
        for num in self.input:
            result *= num  # Множимо елемент на результат
        return result
    def div(self):
        result = self.input[0]  # Перший елемент як початкове значення
        for num in self.input[1:]:  # Проходимо через решту елементів
            if num == 0:
                raise ValueError("Ділення на нуль!")  # Перевірка на ділення на нуль
            result /= num  # Ділимо попереднє значення на наступний елемент
        return result
    
    # def __init__(self, value, tolerance=1e-10):
    #     self.value = value
    #     self.tolerance = tolerance

    def root(self):
        if self.input[0] < 0:
            raise ValueError
        
        guess = self.input[0] / 2  
        while abs(guess * guess - self.input[0]) > self.tolerance:
            guess = (guess + self.input[0] / guess) / 2 
        
        return guess
    
    def sin(self):
        return math.sin(self.angle_radians)

    def cos(self):
        return math.cos(self.angle_radians)

    def tan(self):
        try:
            return math.tan(self.angle_radians)
        except ValueError:
            return "Тангенс не визначений для цього кута."
        
    def cot(self):
        try:
            return 1 / math.tan(self.angle_radians)
        except ValueError:
            return "Котангенс не визначений для цього кута."
    
# sqrt_calculator = Calculator([25])
# print(f"Квадратний корінь: {sqrt_calculator.root()}")
    


# calculator1 = Calculator([1,2,3,4])
# print(calculator1.add())
# print(calculator1.subtract())
# print(calculator1.mul())
# print(calculator1.div())
# angle = 45 
# calculator = Calculator([angle])
# print(f"Синус кута {angle}°: {calculator.sin()}")
# print(f"Косинус кута {angle}°: {calculator.cos()}")
# print(f"Тангенс кута {angle}°: {calculator.tan()}")
# print(f"Котангенс кута {angle}°: {calculator.cot()}")

# To Do: root, exponentiation, trigonometry.
# class SquareRoot:
#     def __init__(self, value, tolerance=1e-10):
#         self.value = value
#         self.tolerance = tolerance

#     def calculate(self):
#         if self.value < 0:
#             raise ValueError
        
#         guess = self.value / 2  
#         while abs(guess * guess - self.value) > self.tolerance:
#             guess = (guess + self.value / guess) / 2 
        
#         return guess

# sqrt_calculator = SquareRoot(25)
# print(f"Квадратний корінь: {sqrt_calculator.calculate()}")


# class TrigCalculator:
#     def __init__(self, angle_degrees):
#         self.angle_degrees = angle_degrees
#         self.angle_radians = math.radians(angle_degrees)  

#     def sin(self):
#         return math.sin(self.angle_radians)

#     def cos(self):
#         return math.cos(self.angle_radians)

#     def tan(self):
#         try:
#             return math.tan(self.angle_radians)
#         except ValueError:
#             return "Тангенс не визначений для цього кута."
        
#     def cot(self):
#         try:
#             return 1 / math.tan(self.angle_radians)
#         except ValueError:
#             return "Котангенс не визначений для цього кута."


# angle = 45 
# calculator = TrigCalculator(angle)
# print(f"Синус кута {angle}°: {calculator.sin()}")
# print(f"Косинус кута {angle}°: {calculator.cos()}")
# print(f"Тангенс кута {angle}°: {calculator.tan()}")
# print(f"Котангенс кута {angle}°: {calculator.cot()}")
calculator = Calculator([10, 5, 2])
print(calculator.subtract())