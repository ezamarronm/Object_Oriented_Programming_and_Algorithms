class Person:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("I'm walking")
    
class Biker(Person):
    def __init__(self,name):
        super().__init__(name)
    def move(self):
        print("I'm Biking")
def main():
    person1 = Person('Eduardo')
    person1.move()

    biker1 = Biker('Daniel')
    biker1.move()

if __name__ == '__main__':
    main()