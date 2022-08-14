from restaurant import Restaurant as res


class Icecream(res):
    ''''''
    def __init__(self, restaurant_name, cuisine_type,  flavours, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = flavours

    def describe_flavour(self):
        for flavour in self.flavours:
            print(flavour)


ice1 = Icecream('1', '2', [1, 2, 3, 4])
ice1.describe_flavour()
