"""
2.2 - Hidden Attributes and Getters/Setters

Goal: You will modify your existing class from previous lessons.

STEP-BY-STEP:
    STEP 1 — Add a Protected Attribute
        Choose one attribute that the object should not be changed directly by outside code (but can still be read if needed).
        Add it using one underscore:
            For example:
                self._protected_value = 10

    STEP 2 - Add a Private Attribute
        Choose another attribute that should be fully hidden from users, because it affects internal logic.
            Add it using two underscores:
            For example:
                self.__private_value = 100

    STEP 3 - Write a Getter Method (for one of your protected or private methods)

    STEP 4 - Write a Setter Method and include a validation check before the return (for one of your protected or private methods)

    STEP 5 — Demonstrate Your Getter and Setter Methods

        After you finish the class:
        - Create an object
        - Try printing the protected attribute
        - Use your getter to read the private attribute
        - Use your setter to change the private attribute
        - Print the private value again to confirm it changed
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

        self.__stamina = 0
        self._strength = 0

    def get_stamina(self):
        return self.__stamina

    def set_stamina(self, stamina):
        if stamina >= 0:
            self.__stamina = stamina
        else:
            print("You can't set negative value")

    def update_pos(self, new_pos):
        prev_pos = self.position
        self.position = new_pos
        return f"You move from {prev_pos} to {new_pos}. New Position: {self.position}"

    def deal_dmg(self, target):
        target.take_dmg(self.attack)
        print(f"{self.name} deal {self.attack} to {target.name}")

    def take_dmg(self, dmg):
        self.hp = self.hp - max(dmg - self.defense, 0)
        print(f"{self.name} has {self.hp} HP left.")
        return self.hp

    def update_inventory(self, item):
        self.inventory.append(item)
        return self.inventory

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

    # for entity in entities_dict:
    #     if entity['hp'] < 30:
    #         print(f"{entity['name']} low HP")
    #
    # entities[0].deal_dmg(character)
    # entities[0].deal_dmg(entities[1])
    # entities[1].deal_dmg(character)
    # print(character.update_pos((0, 5)))
    # print(character.update_pos((4, 5)))
    # print(character.update_pos((-2, 10)))

    print(f"Protected: {entities[0]._strength}")
    print(f"Getter: {entities[0].get_stamina()}")
    entities[0].set_stamina(100)
    print(f"Getter: {entities[0].get_stamina()}")
