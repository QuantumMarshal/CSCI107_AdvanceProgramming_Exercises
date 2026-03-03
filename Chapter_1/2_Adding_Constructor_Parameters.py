"""
Exercise 1.2 - Adding Constructor Parameters

 -- Use vehicles2.py from class as an example to help complete this. --

Goal: Extend the class you created in the previous exercise (1.1) by adding parameters to the constructor (__init__)
      so attributes are set when the object is created. Then manipulate the objects you create with the class.

      This mirrors the example:
            def __init__(self, make, model, color, price, sold=False):

STEP-BY-STEP:
    STEP 1 — Modify Your Existing Class
        Take the class you created in the previous lesson and rewrite its __init__ method so it accepts parameters.
        At least ONE of your parameters should have a DEFAULT/KEYWORD VALUE.
            for example -  we used 'sold = False' as a DEFAULT VALUE


    STEP 2 — Create one Object Using Your New Constructor
        Create at least one object of your class using the new parameters. in the main body of your code.

    STEP 3 — Print the Object’s Attributes in a dictionary

    STEP 4 - Create a loop that allows users to generate more objects using a for loop and store to a list
        You can do this using user input like we did in the example program or assigning them static values during the loop

    STEP 5- Write a conditional to check an attribute value of your choice from an object in the list
            You can do this through user input or by choosing an arbitrary element

                In our example, we used the first element and checked its sold attribute using:
                    if cars_dict[0]['sold']
"""
import faker
import random

class Entity:
    def __init__(self, name, class_type, position = (0,0), hp=100, level=1, attack=10, defense=5, active=True, inventory=[]):
        self.name = name
        self.class_type = class_type
        self.position = position
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.active = active
        self.inventory = inventory

    def update_pos(self, new_pos):
        # self.position = new_pos
        pass

    def deal_dmg(self, target):
        # target.take_dmg(self.attack)
        pass

    def take_dmg(self, dmg):
        # self.hp = self.hp - max(dmg - self.defense, 0)
        pass
    def update_inventory(self, item):
        # self.inventory.append(item)
        pass

if __name__ == '__main__':
    faker = faker.Faker("en_US")
    rand = random.Random()
    character = Entity("Player", "Mage")
    print(character.__dict__)

    num = int(input("Enter the number of entities: "))
    entities = []
    for i in range(num):
        # entity_name = input("Enter the entity name: ")
        # entity_class_type = input("Enter the class type: ")
        entity_name = faker.name()
        entity_class_type = faker.job()
        entity_hp = rand.randint(0, 100)
        entities.append(Entity(entity_name, entity_class_type, hp = entity_hp))

    entities_dict = [i.__dict__ for i in entities]
    print(entities_dict)

    for entity in entities_dict:
        if entity['hp'] < 30:
            print(f"{entity['name']} low HP")