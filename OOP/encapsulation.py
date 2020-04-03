class PollingPlace:
    def __init__(self, identifier, country):
        self.__identifier = identifier
        self.__country = country
        self.__region = None
    
    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self, region):
        if region in self.__country:
            self.__region = region
        else:
            raise ValueError(f'The region is not in {self.__country}')

if __name__ == '__main__':
    pollingPlace1 = PollingPlace(123,['Mexico City', 'Morelos','a'])
    #print(pollingPlace1.__region)

    pollingPlace1.region = 'Morelos'
    pollingPlace1.__region = "Jalisco"
    print(pollingPlace1.__region)
    print(pollingPlace1.region)