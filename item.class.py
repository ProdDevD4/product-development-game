class Item(object):
    def __init__(self, name, attack, armor, weight, price):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.weight = weight
        self.price = price


class Inventory(object):    
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Atk', 'Arm', 'Lb', 'Val']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.attack, item.armor, item.weight, item.price]]))


inventory = Inventory()
inventory.add_item(Item('Sword', 5, 1, 15, 2))
inventory.add_item(Item('Armor', 0, 10, 25, 5))
inventory.print_items()
