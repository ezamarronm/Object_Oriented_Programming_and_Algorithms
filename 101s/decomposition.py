class Car:
    def __init___(self, model, make, color):
        self.model = model
        self.make = make
        self.color = color
        self._status = 'stopped'
        self._motor = Motor(cylinders = 4)
    def accelerate(self, type = 'low'):
        if type == 'fast':
            self._motor.inyect_gasoline(10)
        else:
            self._motor.inyect_gasoline(3)
        self._status = 'moving'
    
    class Motor:
        def __init__(self, cylinders, type = 'gasoline'):
            self.cylinders = cylinders
            self.type = type
            self._temperature = 0
        def inyect_gasoline(self, quantity):
            pass