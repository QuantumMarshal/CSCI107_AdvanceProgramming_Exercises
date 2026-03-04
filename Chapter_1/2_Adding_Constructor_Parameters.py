"""
Exercise 2.1 - Implementing Methods

Goal: Implement at least one method in the class you previously designed in the previous exercises.

STEP-BY-STEP:
    STEP 1 — Choose AT LEAST TWO Methods You Wrote Earlier and Implement It (you can do more)
        Your method MUST:
            Receive at least one parameter
            Modify at least one attribute
            return a message or result

            For example:
                If your class was a GameCharacter a simple method could:
                    def take_damage(self, amount):
                        self.health -= amount
                        return f"{self.name} now has {self.health} HP."

    STEP 2 — Create an instance of the object and Call Your Methods separately

    STEP 3 — Test Your Methods Thoroughly
        Write at least three test cases - for example:

            obj = MyClass("A", "B", "C", 10)
            print(obj.take_damage(5))
            print(obj.take_damage(10))
            print(obj.take_damage(3))
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

    for entity in entities_dict:
        if entity['hp'] < 30:
            print(f"{entity['name']} low HP")

    entities[0].deal_dmg(character)
    entities[0].deal_dmg(entities[1])
    entities[1].deal_dmg(character)
    print(character.update_pos((0, 5)))
    print(character.update_pos((4, 5)))
    print(character.update_pos((-2, 10)))