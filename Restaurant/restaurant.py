class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name.tittle()
        self.cuisine=cuisine
        self.number_served=0

    def describe_restaurant(self):
        print(f'{self.describe_restaurant} serves wonderful {self.name}')

    def open_restaurant(self):
        print(f'Restaurant {self.name} is open. ')

    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine='ice cream'):
        super().__init__(name,cuisine)
        self.flavor=[]

    def show_flavors(self):
        print(f'\nWe have the followings available:')
        for flavor in self.flavors:
            print(f'\n - {flavor.tittle()}')
