#1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __isub__(self, other):
        self.radius -= other.radius
        return self
    
#2
class Complex:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag
    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other: 'Complex') -> 'Complex':
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other: 'Complex') -> 'Complex':
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
    def __truediv__(self, other: 'Complex') -> 'Complex':
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)
    

#3
class Airplane:
    def __init__(self, passengers: int, max_passengers: int, airplane_type: str):
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.airplane_type = airplane_type

    def __eq__(self, other: 'Airplane') -> bool:
        return self.airplane_type == other.airplane_type

    def __lt__(self, other: 'Airplane') -> bool:
        return self.max_passengers < other.max_passengers

    def __le__(self, other: 'Airplane') -> bool:
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other: 'Airplane') -> bool:
        return self.max_passengers > other.max_passengers

    def __ge__(self, other: 'Airplane') -> bool:
        return self.max_passengers >= other.max_passengers

    def __add__(self, other: 'Airplane') -> 'Airplane':
        return Airplane(self.passengers + other.passengers, self.max_passengers + other.max_passengers, self.airplane_type)

    def __iadd__(self, other: 'Airplane') -> 'Airplane':
        self.passengers += other.passengers
        self.max_passengers += other.max_passengers
        return self

    def __sub__(self, other: 'Airplane') -> 'Airplane':
        return Airplane(self.passengers - other.passengers, self.max_passengers - other.max_passengers, self.airplane_type)

    def __isub__(self, other: 'Airplane') -> 'Airplane':
        self.passengers -= other.passengers
        self.max_passengers -= other.max_passengers
        return self
    
#4
    
class Roman:
    def __init__(self, roman_numeral: str):
        self.roman_numeral = roman_numeral

    @staticmethod
    def roman_to_int(roman_numeral: str) -> int:
        roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for i in range(len(roman_numeral) - 1, -1, -1):
            value = roman_to_int_dict[roman_numeral[i]]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

    @staticmethod
    def int_to_roman(integer: int) -> str:
        int_to_roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        result = ''
        for value, numeral in sorted(int_to_roman_dict.items(), reverse=True):
            while integer >= value:
                result += numeral
                integer -= value
        return result

    def __add__(self, other: 'Roman') -> 'Roman':
        return Roman(Roman.int_to_roman(Roman.roman_to_int(self.roman_numeral) + Roman.roman_to_int(other.roman_numeral)))

    def __sub__(self, other: 'Roman') -> 'Roman':
        return Roman(Roman.int_to_roman(Roman.roman_to_int(self.roman_numeral) - Roman.roman_to_int(other.roman_numeral)))

    def __mul__(self, other: 'Roman') -> 'Roman':
        return Roman(Roman.int_to_roman(Roman.roman_to_int(self.roman_numeral) * Roman.roman_to_int(other.roman_numeral)))

    def __truediv__(self, other: 'Roman') -> 'Roman':
        return Roman(Roman.int_to_roman(Roman.roman_to_int(self.roman_numeral) // Roman.roman_to_int(other.roman_numeral)))