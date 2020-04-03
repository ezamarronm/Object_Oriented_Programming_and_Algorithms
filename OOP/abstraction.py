class WashingMachine:
    def __init__(self):
        pass
    def wash(self, temperature = 'hot'):
        self._fill_water_tank(temperature)
        self._add_detergent()
        self._wash()
        self._spin()

    def _fill_water_tank(self, temperature):
        print('Filling the tank')   
    def _add_detergent(self):
        print('Adding Detergent')
    def _wash(self):
        print('Washing your Clothes')
    def _spin(self):
        print('Spinning your Clothes')
    
if __name__ == '__main__':
    washingMachine_1 = WashingMachine()
    washingMachine_1.wash()