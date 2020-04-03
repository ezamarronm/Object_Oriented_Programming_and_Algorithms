class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

if __name__ == '__main__':
    rectangle1 = Rectangle(3,4)
    print(rectangle1.area())

    square1 = Square(5)
    print(square1.area())